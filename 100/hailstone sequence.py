# -------------------------------------------------------------------------------
# Name:         100 Hailstone Sequence
# Purpose:      Shows the sequence in a hailstone calculation
#
# Author:       Douglas Green
#
# Created:      11/10/2014
# Copyright:    (c) Douglas Green 2014
# Licence:      GPL 2.0
# -------------------------------------------------------------------------------


def main():
    x = input('Input a positive integer')
    try:
        x = int(x)
    except ValueError:
        print('failed try again')
        main()
    while x != 4:
        print(int(x))
        if x % 2 == 0:
            x /= 2
        else:
            x = x*3+1

if __name__ == '__main__':
    main()
