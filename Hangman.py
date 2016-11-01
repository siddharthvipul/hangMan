import random #importing random to guess random movie
album = {
	1: 'lord of the rings', 
	2: 'harry potter', 
	3: 'one piece', 
	4: 'dragon ball z', 
	5: 'attack on titans', 
	6: 'full metal alchemist'
	}
number = random.randint(1,6) #taking any random movie form dictionary
movie = album[number]        #storing it in a variable
allowed_attempts = 5
guessed_char = ' '			 #making a stack of guesses taki compare kar sake

while allowed_attempts > 0: 
	mistake = 0

	for letter in movie:
		if letter in guessed_char:
			print (letter)
		else:
			print ('\b'+ '_')    #\b is not woking,  fml
			mistake = mistake + 1
	if mistake == 0:
		print ('Sabaash')
		break
	guess = input('Take your guess: ')
	guessed_char += guess
	if guess not in movie:
	 	allowed_attempts = allowed_attempts - 1
	 	print ('Attempts left: '+ str(allowed_attempts))
	 	if allowed_attempts == 0:
	 		print ('Game over')


