#!/usr/bin/python3
# Trying to create a binary to decimal conversion game

import random


def bin_dec():
    """Function to convert binary to decimal"""
    print("Program to practice Binary to Decimal Conversions")
    print("Enter (Y) to begin, (x) to exit")
    response = input('> ').lower()  # makes input lower case
    if response == 'y':

        while True:
            binary = ""  # Variable to store string of 1,0sss
            for i in range(8):  # Loop through 8 times, (0-7)
                temp = str(random.randint(0, 1))  # generate random 1 or 0
                binary += temp  # concatenate 1s + 0s together 8x to get octet
            # CONVERT BINARY to DECIMAL
            b_digits = list(binary)  # Turn binary string  list IOT access each
            decimal_value = 0  # variable conversion of binary to decimal
            for i in range(8):
                decimal_value += int(b_digits[i]) * (2 ** (7 - i))
            # Display to USER
            print("What is the decimal value?")
            print(binary)  # This is a string, not a number
            answer = input('> ')
            # CHECK ACCURACY OF USER RESPONSE
            if answer == 'x':
                print("Goodbye")
                break
            if int(answer) == decimal_value:
                print("You got it!!")
                print("('x' to exit)\n")
                continue
            elif int(answer) != decimal_value:
                print("Sorry, correct answer is:")
                print(decimal_value)
                print("Enter 'x' to exit at any time.\n")
                continue
    else:
        print("Maybe tomorrow")


def bin_hex():
    """Function to convert Binary to Hexadecimal"""
    print("Binary to Hexadecimal conversion training program")
    print("(Y) to begin | (x) to exit")
    response = input('> ').lower()

    if response == 'y':

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
                print("CORRECT")
            else:
                print("Not quite")
                print(hex_val)
    else:
        print("Maybe tomorrow")


def hex_dec():
    """Function to convert Hexadecimal to Decimal"""
    print("Hexadecimal to Decimal conversion training program")
    print("(Y) to begin | (x) to exit")
    response = input('> ').lower()

    if response == 'y':
        while True:
            random_int = random.randint(0, 255)
            hex_val = format(random_int, '02x')
            print(hex_val)
            print("Decimal Equivalent is?")
            answer = input('> ')

            if answer == 'x':
                break
            elif int(answer) == random_int:
                print("CORRECT")
            else:
                print("Not quite")
                print(random_int)
    else:
        print("Maybe tomorrow")










