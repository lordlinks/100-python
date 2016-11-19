# -------------------------------------------------------------------------------
# Name:         Array find and print
# Purpose:      finds the largest number in an array and prints its location
#
# Author:       Douglas Green
#
# Created:      24/11/2014
# Copyright:    (c) Douglas Green 2014
# Licence:      GPL 2.0
# -------------------------------------------------------------------------------
import sys


def main():
    array = [5, 7, 88, 23, 8, 7, 6, 2, 1, 5, 8, 7, 465, 1, 5, 4, 7, 8, 5, 6, 2, 3, 1, 5, 8, 6]
    largest = 0
    for x in array:
        if x > largest:
            largest = x
    print('the largest number is ' + str(largest) + ' it is at the location ' + str(array.index(largest)))
    sys.exit()


if __name__ == '__main__':
    main()