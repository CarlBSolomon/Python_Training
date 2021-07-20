# This file is for Rock Paper Scissors against the computer. This version plays out a best of option that is decided by the player

import random

print("Welcome to Rock Paper Scissors. The stakes are high")
#initialising the scores of the player and computer
player_score = 0
computer_score = 0
# asking the player to decide the best of number they want to play with
print("PLease enter the best of number you want to play. Keep it odd so that someone actually wins")
winning_score = input()
winning_score = int(winning_score)

# while the scores have not yet reached the max keep playing
while player_score < winning_score and computer_score < winning_score:
	print("Player 1, please enter your choice. Dont let your opponent see it")
	player1_choice = input().lower()
	print(player1_choice)

	random_choice = random.randint(0,2) 
	if random_choice == 0:
		computer_choice = "rock"
	elif random_choice == 1:
		computer_choice = "paper"
	else:
		computer_choice = "scissors"

	# If both players make the same choice then its a draw. 
	if player1_choice == computer_choice:
		if 	computer_choice == 'rock':
			print("Thats a solid draw")
		elif computer_choice == 'paper':
			print("All Drawn up. Better luck next time")
		elif computer_choice == 'scissors':
			print("Lez be honest, that was a draw")

	# If player chooses Rock
	elif player1_choice == 'rock':
		if computer_choice == 'paper':
			print("Computer is the winner. Its all wrapped up")
			computer_score += 1
		elif computer_choice == 'scissors':
			print("Player1 has won. They have rocks to their opponent's head!!")
			player_score += 1
		else:
			print("We are playing RPS. Seems like Computer is not. Invalid entry")

	# if player chooses Paper
	elif player1_choice == 'paper':
		if computer_choice == 'Scissors':
			print("Computer has cut you all up. You Lost!!! Better luck next time")
			computer_score += 1
		elif computer_choice == 'rock':
			print("Player1 has it all covered. You win!!!")
			player_score += 1
		else:
			print("We are playing RPS. Seems like Computer is not. Invalid entry")

	# if player chooses Scissors
	elif player1_choice == 'scissors':
		if computer_choice == 'rock':
			print("Computer has beaten you to it. They win")
			computer_score += 1
		elif computer_choice == 'paper':
			print("Player 1 has shredded all competition. They win")
			player_score += 1
		else:
			print("We are playing RPS. Seems like Computer is not. Invalid entry")

	# if players choose something other than the 3 options
	else:
		if computer_choice == 'rock' or computer_choice == 'scissors' or computer_choice == 'paper':
			print("We are playing RPS. Seems like Player 1 is not. Invalid entry")
		else:
			print("HELLO !!!! We are playing RPS. Seems like neither of you are.")

if player_score > computer_score:
	print(f"FINAL SCORE: Player Score - {player_score}  Computer Score - {computer_score} The Player has won!! ")
else:
	print(f"FINAL SCORE: Player Score - {player_score}  Computer Score - {computer_score} The Computer has won ")