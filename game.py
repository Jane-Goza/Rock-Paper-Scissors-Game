# Import packages to extend Python (just like we extend Sublime, Atom, or VSCode)
from random import randint

# re-import our game variab;es
from gameComponents import gameVars

# define a win or lose function
def winorlose(status):
	#version 1 of function
	# print("Inside winorlose function: status is: ", status)
	print("You", status, " ! Would you like to play again?")
	choice = input("Y / N? ")

	if choice == "N" or choice == "n":
		print("You chose to quit! Better luck next time!")
		exit()
	elif choice == "Y" or choice == "y":
		#reset the player lives and computer lives
		# and reset player choice to False, do our loop restarts

		gameVars.player_lives = gameVars.total_lives
		gameVars.computer_lives = gameVars.total_lives

	else:
		print("Make a valid choice - Y or N")
		# this might generate a bug that we need to fix later
		choice = input("Y / N? ")

# player_choice == False
while gameVars.player_choice is False:
	print("==============*/ RPS GAME */=============")
	print("Computer_Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
	print("Player_Lives:", gameVars.player_lives, "/", gameVars.total_lives)
	print("=========================================")
	gameVars.player_choice = input("Choose rock, paper, or scissors: \n")
	# Version 1, to explain array indexing
	# player_choice = choices[1]
	# print("index 1 in the choice array is " + player_choice + ", which is paper")

	print("Choose your weapon! Or type quit to exit\n")

	gameVars.player_choice = input("Choose rock, paper, or scissors: \n ")
	#player_choice now equals TRUE -> it has a value

	if gameVars.player_choice == "quit":
		print("You chose to quit")
		exit()

	print("user chose " + gameVars.player_choice)

	# this will be the AI choice -> a random pick from the choices array
	gameVars.computer_choice = gameVars.choices[randint(0, 2)]

	print("computer chose: " + gameVars.computer_choice)

	if gameVars.computer_choice == gameVars.player_choice:
		print("tie")

	elif gameVars.computer_choice == "rock":
	    if gameVars.player_choice == "scissors":
	    	print("you lose!")
	    	#verbose way
	    	# player_lives = player_lives - 1
	    	# simplified way
	    	gameVars.player_lives -= 1
	    else:
	    	print("you win!")
	    	gameVars.computer_lives -= 1

	elif gameVars.computer_choice == "paper":
	    if gameVars.player_choice == "scissors":
	    	print("you win!")
	    	gameVars.computer_lives -= 1
	    else:
	    	print("you lose!")
	    	gameVars.player_lives -= 1

	elif gameVars.computer_choice == "scissors":
	    if gameVars.player_choice == "paper":
	    	print("you lose!")
	    	gameVars.player_lives -= 1
	    else:
	    	print("you win!")
	    	gameVars.computer_lives -= 1

	if gameVars.player_lives == 0:
		winorlose("lose")
		
	if gameVars.computer_lives == 0:
		winorlose("win")
		
	print("Player_lives:", gameVars.player_lives)
	print("Computer_lives:", gameVars.computer_lives)

	# map the loop keep running, by setting player_choice back to False
	# unset, so that our loop condition will evaluate to True
	player_choice = False
