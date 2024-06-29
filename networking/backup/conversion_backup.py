#!/usr/bin/python3
# Trying to create a binary to decimal conversion game

import random

# Turn into FUNCTION
print("Let's work on converting binary Octets to their Decimal equivalent.")
print("Enter (Y) to begin, (n) to exit")

response = input('> ').lower()  # makes input lower case

if response == 'y':

    while True:
        binary = ""  # Variable to store string of 1,0sss
        for i in range(8):  # Loop through 8 times, (0-7)
            temp = str(random.randint(0, 1))  # generate random 1 or 0
            binary += temp  # concatenate 1s + 0s together 8x to get octet
        # CONVERT BINARY to DECIMAL
        b_digits = list(binary)  # Turn binary string to list so to access each and convert
        decimal_value = 0  # variable conversion of binary to decimal
        for i in range(8):  # Assist from CHEGG online
            decimal_value += int(b_digits[i]) * (2 ** (7 - i))
        # Display to USER
        print("What is the decimal value?")
        print(binary)  # This is a string, not a number
        answer = input('> ')
        # CHECK ACCURACY OF USER RESPONSE
        if answer == 'x':
            print("Goodbye")
            break
        elif int(answer) == decimal_value:
            print("<< CORRECT >>")
            print("('x' to exit)\n")
        elif int(answer) != decimal_value:
            print("Sorry, correct answer is:")
            print(decimal_value)
            print("Enter 'x' to exit at any time.\n")

else:
    print("Maybe some other time")


def bin_hex(self):
    """Function to convert Binary to Hexadecimal"""
    print("Binary to Hexadecimal conversion training program")
    print("(x) to exit")

    while True:
        random_int = random.randint(0, 255)
        bin_val = format(random_int, '08b')
        hex_val = format(random_int, '02x')
        print(bin_val)
        print("Hex equivalent is?")
        answer = input('> ')

        if answer == 'x':
            break
        elif answer == str(hex_val):
            print("<< CORRECT >>")
        else:
            print("Not quite")
            print(hex_val)


def hex_dec(self):
    """Function to convert Hexadecimal to Decimal"""
    print("Hexadecimal to Decimal conversion training program")
    print("(x) to exit")
    while True:
        random_int = random.randint(0, 255)
        hex_val = format(random_int, '02x')
        print(hex_val)
        print("Decimal Equivalent is?")
        answer = input('> ')

        if answer == 'x':
            break
        elif int(answer) == random_int:
            print("<< CORRECT >>")
        else:
            print("Not quite")
            print(random_int)

