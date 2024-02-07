# Edwin Soetsane's Technical Test

## Overview

Create a backend service for the Fruity Slot game. The game rules and probabilities are defined in JSON
format. Your task includes parsing the JSON, implementing the game logic, using a suitable PRNG for
random number generation, and displaying an output on a basic frontend.

Aim to spend no more than 3 hours on this task.

## Game Rules

1. This game has a single reel which spins and lands on one symbol.
2. The slot machine has 6 symbols: Blank, Cherry, Lemon, Bell, Diamond and Seven. Each symbol
has a weight that determines its probability of appearing.
3. Each symbol is associated with a payout multiplier. For example, if the bet is 1 and a Bell lands,
payout is 2

## Packages

This full-stack web application was created using [Django](https://docs.djangoproject.com/en/5.0/) for the back-end development and [JavaScript](https://www.javascript.com/about) [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) and [HTML](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics) for the front-end development

## Task Details

### 1. Parse the provided JSON containing the game definitions, including symbols, weights, and payouts

![image](https://github.com/Eddie-Soetsane/Fruity-Slot-Game/assets/92805762/2c0e8e4f-72d1-44ac-bc0e-2366e3d8f700)

![image](https://github.com/Eddie-Soetsane/Fruity-Slot-Game/assets/92805762/3b4e88a5-d470-4987-8713-c486b1cf8f99)

### 2. Implement the backend logic for the game based on the JSON definitions

![image](https://github.com/Eddie-Soetsane/Fruity-Slot-Game/assets/92805762/6d92c5e3-dc25-458f-84ae-0ac02be03d81)

This function called game gets the parsed data from the previous function.
I then siphon all the symbols data and put it in a new variable.
I then call another class I created called WeightedRandomNumberGenerator which uses Python's random number generator which is a Pseudorandom Number Generator.
After I called this class I can recieve the result of the random symbol and from that I can workout the total winnings of the user.
I then return the symbol and the total as they will be needed for the front-end.

### 3. Make use of a suitable PRNG (Pseudorandom Number Generator) for generating the result of a spin (please do not implement your own RNG).

![image](https://github.com/Eddie-Soetsane/Fruity-Slot-Game/assets/92805762/e62c9970-e657-4717-be0f-964301ca61fb)

Firstly group all of the weights from the symbols parsed and put them into variable self.weights.
I then add up the total sum of these weights as this will be used later for probability in conjunction with the Pseudorandom Number Generator.
I then make a third variable that would contain all the symbols and their corresponding payouts. Like seen in the function about this is used to get the correct
multiplier that would be put up against the bet.
I create a new function that calculates what symbol will be picked. I firstly find a random number between 1 and the total amount of weights.
I then create a counter weight this will be used to implement the probability and figure out which symbol is given.
I scan through all the weights to find the moment when the randomNumber is less than or equal to the counter weights and then the symbol that correspondes to
to the number and probability is given.
I created a get payout function so that the correct payout multipler can be applied in the fruity slot class.

### 4.Create a basic console application or web interface to display the output of the game. Thefrontend is not a priority, but if you would like to demonstrate frontend skills, feel free to run with it.

![image](https://github.com/Eddie-Soetsane/Fruity-Slot-Game/assets/92805762/37f54eec-c9db-4034-8b74-33642ed0e1db)

The following was my console test making sure everything is working correctly.

The following are videos showing the front-end in action. Due to the limited time allowed it is basic but allows me to improve on the project in the future.
(The music is not actually in the game but its a feature I would like to add in the future)

https://github.com/Eddie-Soetsane/Fruity-Slot-Game/assets/92805762/2250a528-0686-4025-b39a-9fa2ac52b369


https://github.com/Eddie-Soetsane/Fruity-Slot-Game/assets/92805762/3d5a3bab-8075-4da2-80c8-16e0335664bd

Coding for spinning and how the front and back-end was communicating:

![image](https://github.com/Eddie-Soetsane/Fruity-Slot-Game/assets/92805762/4237914f-fa21-4c1d-98fc-aa7b98b47a58)

![image](https://github.com/Eddie-Soetsane/Fruity-Slot-Game/assets/92805762/cc847056-f6bb-4f5e-839c-44675ca6cda1)

![image](https://github.com/Eddie-Soetsane/Fruity-Slot-Game/assets/92805762/a763bf84-5c65-4bb8-9962-cfc98932680f)
![image](https://github.com/Eddie-Soetsane/Fruity-Slot-Game/assets/92805762/0efdc215-4c7b-456c-aba0-978da357f350)


### 5. You are free to use any programming language and technology stack.

Like previously stated above I used Python Django for my back-end with Javascript, html and css for my front-end

## Conclusion

I hope that you enjoyed my Fruit Slot Tech Demo :)










