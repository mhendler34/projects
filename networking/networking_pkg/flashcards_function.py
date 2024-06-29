#!/usr/bin/python3


def flash_cards(subject, dictionary):
    """FUNCTION to spin through k,v pairs to quiz user on subject matter"""

    print("==== LET'S TRAIN ====")
    print(f"This session's training topic: {subject.upper()}")
    print("(x) at any time to Exit")

    wrong_answers = []
    i = 0
    answer = ""
    while i < len(dictionary):
        if answer == 'x':
            break
        for key in dictionary:
            i += 1
            print(f"\n{key}")
            answer = input('> ').lower()
            value = dictionary[key]
            if answer == 'x':
                break
            elif answer == value:
                print("<< CORRECT >>")
            else:
                print("Not quite")
                print(value)
                wrong_answers.append(key)
                wrong_answers.append(value)
    print(f"\n{subject.upper()} missed:\n")
    print(wrong_answers)
