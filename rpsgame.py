#rock paper scissors
#computer opponent plays
from random import randint
#list of play option
t=["Rock","Paper","Scissors"]
#assigning random play to computer
computer=t[randint(0,2)]

player=False

while player==False:
	player=input("Rock,Paper,Scissors\n")
	if player==computer:
		print("Tie")
	elif player=="Rock":
		if computer=="paper":
			print("You lose",computer,"covers",paper)
		else:
			print("You win",player,"smashes",computer)
	elif player=="paper":
		if computer=="Scissors"	:
			print("You lose",computer,"cuts",player)
		else:
			print("you win",player,"covers",computer)
	elif player=="Scissors":
		if computer=="Rock":
			print("you lose",computer,"smashes",player)
		else:
			print("you win",player,"cuts",computer)
	else:
			print("Not a valid play")


	player = False
	computer = t[randint(0,2)]
		