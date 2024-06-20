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
        print("Convert the Binary Octet to Decimal Equivalent")
        print(binary)  # This is a string, not a number
        print("Enter decimal equivalent below")

        # CONVERT BINARY to DECIMAL
        b_digits = list(binary)  # Turn binary string to a list IOT access each
        decimal_value = 0  # Variable used in conversion of binary to decimal

        for i in range(8):
            decimal_value += int(b_digits[i]) * (2 ** (7 - i))

        # GET USER RESPONSE AND CHECK ACCURACY
        answer = int(input('> '))

        if answer == decimal_value:
            print("That's right! You got it !!")
            print("Would you like to play again? (Y/n)")
            response = input('> ').lower()
            if response == 'y':
                continue
            else:
                print("Good work for today!")
                break

        if answer != decimal_value:
            print("Sorry, that's not quite right.")
            print("The correct answer is:")
            print(decimal_value)
            print("Would, you like to play again? (Y/n)")
            response = input('> ').lower()
            if response == 'y':
                continue
            else:
                print("Good work for today!")
                print("Work on it tomorrow")
                break

else:
    print("Maybe some other time")
