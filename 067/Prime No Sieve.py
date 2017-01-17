# -------------------------------------------------------------------------------
# Name:         Prime No Sieve.py
# Purpose:      Finds prime numbers by removing factors
#
# Author:       Douglas Green
#
# Created:      17/1/2017
# Copyright:    (c) Douglas Green 2017
# Licence:      GPL 2.0
# -------------------------------------------------------------------------------


while __name__ == '__main__':
	greatest = int(input('Please input the largest number you wish to consider for a prime'))
	table = []
	for x in range(0, (greatest + 1), 1):
		table.append(x)
	for x in table:
		if x >= 2:
			y = x
			while (y + x) < greatest:
				y += x
				try:
					table.remove(y)
				except ValueError:
					pass
	del table[-1]
	print(table)
