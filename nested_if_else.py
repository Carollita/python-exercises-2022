winning_number = 8
user_number = int(input('Guess a number between 0 and 10: '))

if user_number == winning_number:
	print('You Win!!!')

else:
	if user_number > winning_number:
		print('Too high')
	else:
		print('Too low')