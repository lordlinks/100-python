# -------------------------------------------------------------------------------
# Name:         014 Collatz Conjecture
# Purpose:      Show the sequence for the Collatz algorithm
#
# Author:       Douglas Green
#
# Created:      4/01/2017
# Copyright:    (c) Douglas Green 2017
# Licence:      GPL 2.0
# -------------------------------------------------------------------------------


def input_required():
	try:
		u_int = input('Please enter a positive integer')
		conjecture(int(u_int))
	except TypeError:
		print('unidentified input please try again')
		input_required()
	except ValueError:
		print('unidentified input please try again')
		input_required()


def conjecture(number):
	x = number
	i = 0
	while x > 1:
		print(x)
		i += 1
		if x % 2 == 0:
			x = int(x / 2)
		else:
			x = (x * 3) + 1
	print(x)
	print('The calculation required ' + str(i) + ' iterations.')


if __name__ == '__main__':
	input_required()
