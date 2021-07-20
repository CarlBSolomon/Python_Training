# This file is for Rock Paper Scissors

print("Welcome to Rock Paper Scissors. The stakes are high")
print("Player 1, please enter your choice. Dont let your opponent see it")
player1_choice = input().lower()
print(player1_choice)
# print("     \n\n" * 60)
print("PLayer 2, please enter your choice. Remember protect it from peering eyes!!")
player2_choice = input().lower()

# If both players make the same choice then its a draw. 
if player1_choice == player2_choice:
	if 	player2_choice == 'rock':
		print("Thats a solid draw")
	elif player2_choice == 'paper':
		print("All Drawn up. Better luck next time")
	elif player2_choice == 'scissors':
		print("Lez be honest, that was a draw")

# If player chooses Rock
elif player1_choice == 'rock':
	if player2_choice == 'paper':
		print("PLayer 2 is the winner. Its all wrapped up")
	elif player2_choice == 'scissors':
		print("Player1 has won. They have rocks to their opponent's head!!")
	else:
		print("We are playing RPS. Seems like Player 2 is not. Invalid entry")

# if player chooses Paper
elif player1_choice == 'paper':
	if player2_choice == 'Scissors':
		print("PLayer 2 has cut you all up. You Lost!!! Better luck next time")
	elif player2_choice == 'rock':
		print("Player1 has it all covered. You win!!!")
	else:
		print("We are playing RPS. Seems like Player 2 is not. Invalid entry")

# if player chooses Scissors
elif player1_choice == 'scissors':
	if player2_choice == 'rock':
		print("PLayer 2 has beaten you to it. They win")
	elif player2_choice == 'paper':
		print("Player 1 has shredded all competition. They win")
	else:
		print("We are playing RPS. Seems like Player 2 is not. Invalid entry")

# if players choose something other than the 3 options
else:
	if player2_choice == 'rock' or player2_choice == 'scissors' or player2_choice == 'paper':
		print("We are playing RPS. Seems like Player 1 is not. Invalid entry")
	else:
		print("HELLO !!!! We are playing RPS. Seems like neither of you are.")