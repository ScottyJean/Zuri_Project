# Zuri_Project
Rock-Paper-Scissors Game
Rock-Paper-Scissors is a simple two-player game where, at a signal, players make figures with their hands, representing a rock, a piece of paper, or a pair of scissors. The winner is determined according to a set of rules. You can find the official rules under the Resources.

A brief summary:
If the two players choose the same “character” it’s a tie, and the game repeats
Rock beats Scissors
Paper beats Rock
Scissors beats Paper
I have created a simple version of this game with Python. In my version, one player will be controlled by the computer and the other player controlled by the user (i.e CPU vs Player). I made use of the inbuilt Python module random and its choice method.

Instructions:

Create a new Python file and call it main.py. Inside it you'll create your game.
Create a list to store all possible options:
"R" for "rock", 
"P" for "paper", 
"S" for "scissors".
When the program is run, ask the user to pick an option between "R", "P" or "S"
If user input is invalid (not amongst our options), print an error, and ask for their input again (should be a loop)
Use the `choice` function from the inbuilt Python `random` module to make a choice for CPU player(computer).
Print both player's moves in the format: `Player (Rock) : CPU (Paper)`
Check both player's moves: 
If there is a winner, print the winner, and the program ends. 
If it's a tie (the computer and player pick the same move), restart the game from step 3


Resources:
https://www.wikihow.com/Play-Rock%2C-...
https://en.wikipedia.org/wiki/Rock_paper_scissors
https://www.w3schools.com/python/module_random.asp
https://pynative.com/python-random-choice/
Zuri:Introduction to Python Modules
Zuri:For Loops 
Zuri:While Loops
