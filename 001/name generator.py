# -------------------------------------------------------------------------------
# Name:         001 Name Generator
# Purpose:      Generates a two word name from a list of first and last names
#
# Author:       Douglas Green
#
# Created:      22/11/2014
# Copyright:    (c) Douglas Green 2014
# Licence:      GPL 2.0
# -------------------------------------------------------------------------------
import random
import sys
import tkinter


def main():
    """Asks user what they want to do and then progresses the program"""
    print("What would you like to do?")
    print("1 - Generate name.")
    print("2 - Add first name.")
    print("3 - Add last name.")
    print("4 - Show all the names")
    print("5 - Exit.")
    sel = input("Enter selection.")
    selector(sel)


def open_file(filename):
    """open_file(filename) string -> list
    where filename includes extension and returns the file as an object"""
    csv_file = open(filename, "r")
    file_read = csv_file.read()
    split_words = file_read.split(",")
    csv_file.close()
    return split_words


def name_formatter(file):
    """write_file(file) string -> null
    filename -- enter in file you wish to overwrite with new data
    data -- the information that is to be written to file
    """
    out_string = ''
    new_name = input("Enter new name.")
    new_name = new_name.capitalize()
    data = open_file(file)
    for x in data:
        out_string += (x + ',')
    out_string += new_name
    csv_file = open(file, "w")
    csv_file.write(out_string)
    csv_file.close()


def selector(sel):
    """selector(sel) string -> null
    Takes in raw input checks to see if it is valid then calls the
    appropriate method"""
    try:
        choice = int(sel)
    except ValueError:
        print("Incorrect selection please select again")
        main()
    if choice == 1:
        first = open_file("first.csv")
        last = open_file("last.csv")
        first = str(random.choice(first))
        last = str(random.choice(last))
        print(first+' '+last)
        main()
    elif choice == 2:
        name_formatter('first.csv')
        main()
    elif choice == 3:
        name_formatter('last.csv')
        main()
    elif choice == 4:
        firstname = open_file('first.csv')
        print('The first names are.')
        print(' ')
        print(firstname)
        print(' ')
        lastname = open_file('last.csv')
        print('The last names are.')
        print(' ')
        print(lastname)
        main()
    elif choice == 5:
        sys.exit()
    else:
        print("You have made an incorrect selection please try again.")
        main()


if __name__ == '__main__':
    main()
