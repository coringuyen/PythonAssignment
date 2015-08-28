import random

while True:
	guess = input("Guess a number between 1-10: ")
	
	if guess == random.randint(0,10):
		print('You Are Correct!!')
		break
	else: 
		print('Try Again')
		
	

