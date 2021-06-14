import random, sys
print("Welcome to the Rock, Paper, Scissors game!")

wins = 0
ties = 0
losses = 0

while True: # Whole Game Loop
    while True: # Result and Giving input loop
        print(" Your Game Tracker :")
        print("Wins : " + str(wins), "Ties : " + str(ties), "Losses : " + str(losses), sep =" | ")
        print("Type Your move : (R)ock, (P)aper, (S)cissor or (Q)uit")
        user_input = input() # User chooses its move
        if user_input == "R" or user_input == "P" or user_input == "S":
            break # Starting the Game
        elif user_input == "Q":
            sys.exit() # Quiting the Game
    if user_input == "R" or user_input == "P" or user_input == "S":


    # Displaying user move.
        if user_input == "R":
            print("Rock versus...")
        elif user_input == "P":
            print("Paper versus...")
        elif user_input == "S":
            print("Scissor versus...")


    # Computer choosing its move.
        comp_choose = random.randint(1, 3)
        if comp_choose == 1:
            comp_input = "R"
            print("...Rock")
        elif comp_choose == 2:
            comp_input = "P"
            print("...Paper")
        elif comp_choose == 3:
            comp_input = "S"
            print("...Scissor")


    # Deciding the result of the game.


        # If there are Ties
        if user_input == comp_input :
            ties = ties + 1
            print("That is A tie.")


        # If the user Wins
        elif user_input == "R" and comp_input == "S":
            wins = wins + 1
            print(" You won this time! ")
        elif user_input == "P" and comp_input == "R":
            wins = wins + 1
            print(" You won this time! ")
        elif user_input == "S" and comp_input == "P":
            wins = wins + 1
            print(" You won this time! ")


        # If the user Losses
        elif user_input == "R" and comp_input == "P":
            losses = losses + 1
            print("You lost this time!")
        elif user_input == "P" and comp_input == "S":
            losses = losses + 1
            print("You lost this time!")
        elif user_input == "S" and comp_input == "R":
            losses = losses + 1
            print("You lost this time!")