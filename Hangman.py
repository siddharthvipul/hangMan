import sys
import os
movie = sys.argv[1]
os.system("clear")
allowed_attempts = 7
guessed_char = ' '
while allowed_attempts > 0: 
	mistake = 0

	for letter in movie:
		if letter in guessed_char:
			print (letter)
		else:
			print ('\b'+ '_')
			mistake = mistake + 1
	if mistake == 0:
		print ('Well Done')
		break
	guess = input('Take your guess: ')
	guessed_char += guess
	if (guess not in movie) and (allowed_attempts > 0):
	 	allowed_attempts = allowed_attempts - 1
	 	print ('Attempts left: '+ str(allowed_attempts))
	if allowed_attempts == 0:
	 	print ('Game over')
	 	break