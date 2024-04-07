import random

# WINNING PATTERNS
win = [("scissors","paper"), ("paper","rock"), ("rock","scissors")]

# INSTRUCTIONS
print("There are 6 rounds.\nYou are playing against SONA.\nYou will win if you have a higher point.\nEnter scissors, paper, or rock.\n")

# CHOICES FOR SONA TO CHOOSE FROM
choices = ["scissors", "paper", "rock"]

# TO COUNT THE NUMBER OF ROUNDS
count = 0
# TO COUNT THE PLAYER'S POINTS
playerPoints = 0
# TO COUNT SONA'S POINTS
SONAPoints = 0

# WHILE LOOP TO SET THE NUMBER OF ROUNDS
while count != 6:
    # INPUT FOR PLAYER'S CHOICE
    player = input("What is your move? ")
    
    # SONA RANDOMLY SELECT CHOICE FROM CHOICES LIST
    SONA = random.choice(choices)
    # PRINT SONA'S INITIAL MOVE
    print("SONA's move:", SONA)

    # DIFFERENT CHOICES
    if player != SONA:
        # CHECK FOR PATTERNS
        playerWins = (player,SONA)
        SONAWins = (SONA,player)
        if playerWins in win:
            if playerWins == win[0]:
                print("Scissors cuts paper \nYou Won!")
            elif playerWins == win[1]:
                print("Paper covers rock \nYou Won!")
            elif playerWins == win[2]:
                print("Rock crushes scissors \nYou Won!")
            playerPoints += 1
        elif SONAWins in win:
            if SONAWins == win[0]:
                print("Scissors cuts paper \nSONA Wins!")
            elif SONAWins == win[1]:
                print("Paper covers rock \nSONA Wins!")
            elif SONAWins == win[2]:
                print("Rock crushes scissors \nSONA Wins!")
            SONAPoints += 1
        # PLAYER DID NOT INPUT scissors, paper, or rock
        else:
            print("Invalid response \nSONA Wins!")
            SONAPoints += 1

    # DRAW, SAME CHOICES
    elif player == SONA:
        print("Draw, Player and SONA get 1 point")
        playerPoints += 1
        SONAPoints += 1

    # EMPTY LINE FOR A NEATER/CLEARER VIEW
    print("")

    # INCREMENT TO CONTROL THE NUMBER OR ROUNDS
    count += 1

# COMPARISON TO DETERMINE WHO IS THE CHAMPION
if playerPoints > SONAPoints:
    print("You are the champion! 🏆")
elif playerPoints == SONAPoints:
    print("You are both champions!! 🏆🏆")
else:
    print("SONA is the champion, Try Again! 💻")
