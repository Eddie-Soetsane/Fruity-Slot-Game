from django.db import models
import json
import random

class WeightedRandomNumberGenerator:
    def __init__(self, data):
        self.weights = {symbol["name"]: symbol["weight"] for symbol in data}
        self.totalWeights = sum(self.weights.values())
        self.payouts = {symbol["name"]: symbol["payout"] for symbol in data}

    def nextSymbol(self):
        randomNumber = random.randint(1, self.totalWeights)
        cWeight = 0
        for symbol, weight in self.weights.items():
            cWeight += weight
            if randomNumber <= cWeight:
                return symbol

    def getPayout(self, symbol):
        return self.payouts.get(symbol, 0)

class FruitySlot(models.Model):
    balance = models.FloatField(default=0)

    @classmethod
    def parseData(cls):
        json_data = '''
        {
            "GameDefinition": {
                "Symbols": [
                {"name": "Blank", "weight": 50, "payout": 0},
                {"name": "Cherry", "weight": 60, "payout": 0.5},
                {"name": "Lemon", "weight": 40, "payout": 1},
                {"name": "Bell", "weight": 20, "payout": 2},
                {"name": "Diamond", "weight": 10, "payout": 5},
                {"name": "Seven", "weight": 1, "payout": 15}
            ]
        }
        }
        '''
        parsed_data = json.loads(json_data)
        return parsed_data
    
    @classmethod
    def game(cls, bet):
        data = cls.parseData()
        symbolData = data["GameDefinition"]["Symbols"]
        generator = WeightedRandomNumberGenerator(symbolData)
        symbol = generator.nextSymbol()
        payout = generator.getPayout(symbol)
        total = bet * payout
        cls.update_balance(total)
        return symbol, total

    @classmethod
    def update_balance(cls, total):
        obj, created = cls.objects.get_or_create(pk=1)
        obj.balance += total
        obj.save()  

    @classmethod
    def get_balance(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj.balance

    @classmethod
    def set_balance(cls, new_balance):
        obj, created = cls.objects.get_or_create(pk=1)
        obj.balance = new_balance
        obj.save()