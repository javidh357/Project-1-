import random
computer=random.choice([1,2,3])

n=input("Enter your choies : ")
names ={"s":1,"w":2,"g":3}
reversed_names={1:"Snake", 2:"Water",3:"Gun"}

you=names[n]
print(f"You chose{reversed_names[you]} \ncomputer chose {reversed_names[computer]}")


if( computer == you):
	print("Its a Draw")

else:
	if(computer==1 and you==2):
		print( "You lose")

	elif(computer==2 and you==1):
		print("You win")

	elif(computer==3 and you==2):
		print("You win")

	elif(computer==3 and you==1):
		print("You lose")

	elif(computer==2 and you==3):
		print("You lose")

	elif(computer==1 and you==3):
		print("You win")

