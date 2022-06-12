import random

def start_game():
    
    # Welcome to the game
    print("""
    Welcome to Rock, Paper, Scissors!!\n
    These are the rules of the game:
    - Rock vs Paper = Paper wins
    - Rock vs Scissors = Rock wins
    - Paper vs Scissors = Scissors wins
        """)

    # list of all possible options
    options = ["R", "P", "S"]

    # ask player to input an option
    player = input("Enter your choice: ")
    while player not in options:
        player = input("Please enter a valid response: ")


    # if player inputs R, rock is chosen
    # if player inputs P, paper is chosen 
    # if player inputs S, scissors is chosen     
    if player == "R":
        player = "Rock"
    elif player == "P":
        player = "Paper"
    else:
        player = "Scissors"

    # computer selects randomly from the available options
    Gamer1 = random.choice(options)

    # if computer chooses R, the computer chooses rock
    # if computer chooses P, the computer chooses paper
    # if computer chooses S, the computer chooses scissor
    if Gamer1 == "R":
        Gamer1 = "Rock"
    elif Gamer1 == "P":
        Gamer1 = "Paper"
    else:
        Gamer1 = "Scissors"

    # print options chosen by the player and computer
    print(f"\nPlayer ({player}) : CPU({Gamer1})")


    # if both player and computer choose the same option, it is a tie
    # The game would restart until one of the players wins
    if player == Gamer1:
        print("It's a tie! Try again!")
        start_game()

    # if player chooses rock and computer chooses paper, player wins
    # if player chooses rock and computer chooses scissors, player loses
    elif player == "Rock":
        if Gamer1 == "Scissors":
            print(f"Rock beats scissors! Player({player}) wins!\n")
        else:
            print(f"Paper beats rock! CPU({Gamer1}) wins!\n")

    # if player chooses paper and computer chooses rock, player wins
    # if player chooses paper and computer chooses scissors, player loses
    elif player == "Paper":
        if Gamer1 == "Rock":
            print(f"Paper beats rock! Player({player}) wins!\n")
        else:
            print(f"Scissors beats paper! CPU{(Gamer1)} wins!\n")

    # if player chooses scissors and computer chooses rock, player loses
    # if player chooses scissors and computer chooses paper, player wins
    elif Gamer1 == "Paper":
        print(f"Scissors beats paper! Player({player}) wins!\n")
    else:
        print(f"Rock beats scissors! CPU({Gamer1}) wins!\n")
       
       
# function to start the game
start_game()
