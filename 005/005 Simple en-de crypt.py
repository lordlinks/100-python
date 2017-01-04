# -------------------------------------------------------------------------------
# Name:         005 Simple encrypt/decrypt method
# Purpose:      Take a simple message and hide it in scrambled text
#
# Author:       Douglas Green
#
# Created:      4/1/2017
# Copyright:    (c) Douglas Green 2017
# Licence:      GPL 2.0
# -------------------------------------------------------------------------------
import string
import random


def usr_input():
	"""
Gets the appropriate information form the user
:return: none
"""
	try:
		msg = input('Type your secret message here:')
		off = int(input('choose and offset, type a positive number here:'))
		fill = int(input('How many filling characters would you like to use:'))
		encrypter(int(off), int(fill), str(msg))
	except TypeError:
		print('Unknown characters please try again')
		usr_input()
	except ValueError:
		print('Unknown characters please try again')
		usr_input()


def ch_decrypt():
	try:
		offset = int(input('What is the offset for the message?'))
		fill = int(input('What is the fill setting'))
		msg = input('What is the encrypted message?')
		decrypter(offset, fill, msg)
	except TypeError:
		print('Incorrect input please start over')
		ch_decrypt()
	except ValueError:
		print('Incorrect input please start over')
		ch_decrypt()


def choice():
	ch1 = input('To encrypt type "1" to decrypt type "2"')
	if ch1 == "1":
		usr_input()
	elif ch1 == "2":
		ch_decrypt()
	else:
		print('Incorrect input try again')
		choice()


def encrypter(offset, fill, message):
	"""
Encrypts the message and prints the encrypted form to the console.
:param offset: int
:param fill: int
:param message: string
:return: none
"""
	out_str = ""
	# Add offset characters
	out_str += randomizer(offset)
	for x in message:
		# for each character insert filler characters in between
		out_str += x + randomizer(fill)
	print(out_str)


def decrypter(offset, fill, message):
	"""
decrypts a super secret message
:param offset: int
:param fill: int
:param message: string
:return: none
"""
	# Use the string functions to decrypt the message
	print(message[offset:len(message):(fill + 1)])


def randomizer(number):
	"""
Returns string of random characters
:param number: int
:return: string
"""
	x = number
	y = ""
	# How many randomised letters do we need
	while x > 0:
		# From the range of letters digits and spaces select one
		y += random.choice(string.ascii_letters + string.digits + " ")
		x -= 1
	return y


if __name__ == '__main__':
	# Start the program
	choice()
