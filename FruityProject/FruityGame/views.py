from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import FruitySlot

def play_game(request):
    return render(request, 'FruityGame/play_game.html')

def play(request):
    if request.method == 'POST':
        bet = float(request.POST.get('bet'))
        game = FruitySlot.objects.first()  
        symbol, balance = game.game(bet)
        return JsonResponse({'symbol': symbol, 'balance': balance})
    return render(request, 'play.html')