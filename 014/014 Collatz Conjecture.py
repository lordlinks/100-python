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
	"""Get the input form the user"""
	try:
		# If the input is an int then pass that to the conjecture function
		u_int = input('Please enter a positive integer')
		conjecture(int(u_int))
	except TypeError:
		# In the case of a type error display message and restart the process
		print('unidentified input please try again')
		input_required()
	except ValueError:
		# In the case of a Value error (i.e. float or binary number) display message and start again
		print('unidentified input please try again')
		input_required()


def conjecture(number):
	"""Algorithm for processing the conjecture takes in an int and returns nothing"""
	# Copy our number to the variable x so we can reassign it within the function
	x = number
	# Create an iterative so we can tell how many times the loop was activated
	i = 0
	while x > 1:
		# What is the current number
		print(x)
		# Advance the increment count
		i += 1
		if x % 2 == 0:
			# If number dividable by 2 then divide by 2
			x = int(x / 2)
		else:
			# Otherwise multiply by 3 and add 1
			x = (x * 3) + 1
	# We have hit the ground state where our number = 1
	print(x)
	# Tell us how many times we had to iterate just for fun
	print('The calculation required ' + str(i) + ' iterations.')


if __name__ == '__main__':
	input_required()
