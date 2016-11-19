# -------------------------------------------------------------------------------
# Name:        fizz buzz
# Purpose:
#
# Author:      Douglas Green
#
# Created:     10/10/2014
# Copyright:   (c) Douglas Green 2014
# Licence:     GPL 2.0
# -------------------------------------------------------------------------------


def main():
    x = 0
    while x <= 100:
        x += 1
        if x % 3 == 0 and x % 5 == 0:
            print('FizzBuzz')
        elif x % 3 == 0:
            print('Fizz')
        elif x % 5 == 0:
            print('Buzz')
        else:
            print(x)

if __name__ == '__main__':
    main()
