#!/usr/bin/python3


def mod5_menu():
    """Function to display training topics for Module 5"""
    print("Which module 5 topic to train on? | (x) to Main Menu")
    print("1)   Ethernet Cable Standards")
    print("2)   Ethernet Fiber Standards")
    print("3)   Twisted Pair Standards")
    print("4)   T568-A pin outs")
    print("5)   T568-B pin outs")
    print("6)   Terms and Definitions")
    print("\n Type in number of topic to select it")


def ethernet_cable_standards():
    """FUNCTION to train on ethernet cable standards and their metrics"""

    cable_standards = {'10BASE-T-Mbps': '10mbps', '10BASE-T-dist': '100m',
                        '10BASET-media': 'cat3', '10BASET-pairs': '2',
                        '100BASET-Mbps': '100mbps', '100BASET-dist': '100m',
                        '100BASET-media': 'cat5', '100BASET-pairs': '2',
                        '100BASETX-Mbps': '100mbps', '100BASETX-dist': '100m',
                        '100BASETX-media': 'cat6', '100BASETX-pairs': '2',
                        '1000BASET-Mbps': '1000mbps', '1000BASET-dist': '100m',
                        '1000BASET-media': 'cat5', '1000BASET-pairs': '4',
                        '2.5GBASET-Mbps': '2500mbps', '2.5GBASET-dist': '100m',
                        '2.5GBASET-media': 'cat5e', '2.5GBASET-pairs': '4',
                        '5GBASET-Mbps': '5000mbps', '5GBASET-dist': '100m',
                        '5GBASET-media': 'cat6', '5GBASET-pairs': '4',
                        '10GBASET-Mbps': '10000mbps', '10GBASET-dist': '100m',
                        '10GBASET-media': 'cat6/7', '10GBASET-pairs': '4',
                        '40GBASET-Mbps': '40000mbps', '40GBASET-dist': '30m',
                        '40GBASET-media': 'cat8', '40GBASET-pairs': '4'}

    print("Train on ethernet cable standards?")
    print("Enter (Y) to being | (x) to exit")
    response = input('> ').lower()

    if response == 'y':
        print("==== LET'S TRAIN ====")
        print("Enter metric associated with ethernet cable standard")

        wrong_standard = []
        i = 0
        answer = ""
        while i < len(cable_standards):

            if answer == 'x':
                break
            for key in cable_standards:
                i += 1
                print(f"\n{key}")
                answer = input('> ').lower()
                value = cable_standards[key]
                if answer == 'x':
                    break
                elif answer == value:
                    print("CORRECT")
                else:
                    print(f"Not Quite: {value}")
                    wrong_standard.append(key)
                    wrong_standard.append(value)
        print("===========")
        print("Ethernet Standards Missed")
        print(wrong_standard)
        print()
        mod5_menu()
        response = input('> ')
        if response == '1':
            ethernet_cable_standards()
        elif response == '2':
            ethernet_fiber_standards()
        elif response == '3':
            twisted_pair_standards()
        elif response == '4':
            pin_outs_T568A()
        elif response == '5':
            pin_outs_T568B()
        elif response == '6':
            cabling_terms()
        else:
            print("Back to main menu")

    else:
        print("Back to main menu")


def ethernet_fiber_standards():
    """Function to train on ethernet Fiber Optic standards"""
    fiber_standards = {'100BASE-SX-Mbps': '100mbps', '100BASE-SX-dist': '300m',
                       '100BASE-SX-media': 'mmf', '100BASE-FX-Mbps': '100mbps',
                       '100BASE-FX-dist': '2000m', '100BASE-FX-media': 'mmf',
                       '1000BASE-SX-Mbps': '1000mbps', '1000BASE-SX-dist': '550m',
                       '1000BASE-LX-Mbps': '1000mbps', '1000BASE-LX-dist-mmf':
                       '550m', '1000BASE-LX-dist-smf': '5000m',
                       '1000BASE-LX-media': 'mmf/smf', '10GBASE-SR-Mbps': '10000mbps',
                       '10GBASE-SR-dist': '300m', '10GBASE-SR-media': 'mmf',
                       '10GBASE-LR-Mbps': '10000mbps', '10GBASE-LR-dist': '10000m',
                       '10GBASE-LR-media': 'smf'}

    print("Train on Ethernet Fiber Standards?")
    print("Enter (Y) to being | (x) to exit")
    response = input('> ').lower()

    if response == 'y':
        print("==== LET'S TRAIN ====")
        print("Enter metric associated with Ethernet Fiber Standard")

        wrong_standard = []
        i = 0
        answer = ""
        while i < len(fiber_standards):

            if answer == 'x':
                break
            for key in fiber_standards:
                i += 1
                print(f"\n{key}")
                answer = input('> ').lower()
                value = fiber_standards[key]
                if answer == 'x':
                    break
                elif answer == value:
                    print("CORRECT")
                else:
                    print(f"Not Quite: {value}")
                    wrong_standard.append(key)
                    wrong_standard.append(value)
        print("===========")
        print("Ethernet Fiber Standards Missed")
        print(wrong_standard)
        print()
        mod5_menu()
        response = input('> ')
        if response == '1':
            ethernet_cable_standards()
        elif response == '2':
            ethernet_fiber_standards()
        elif response == '3':
            twisted_pair_standards()
        elif response == '4':
            pin_outs_T568A()
        elif response == '5':
            pin_outs_T568B()
        elif response == '6':
            cabling_terms()
        else:
            print("Back to main menu")

    else:
        print("Back to main menu")


def twisted_pair_standards():
    """Function to train on twisted pair category standards"""

    twisted_pair = {'Cat3-Mbps': '10Mbps', 'Cat5-Mbps': '100Mbps',
                    'Cat5e-Mbps': '1000Mbps', 'Cat6-Mbps': '1Gbps/10Gbps',
                    'Cat6a-Mbps': '10Gbps', 'Cat7-Mbps': '10Gbps/100Gbps',
                    'Cat8-Mbps': '25Gbps/40Gbps'}

    print("Train on Twisted Pair Standards?")
    print("Enter (Y) to being | (x) to exit")
    response = input('> ').lower()

    if response == 'y':
        print("==== LET'S TRAIN ====")
        wrong_standard = []
        i = 0
        answer = ""
        while i < len(twisted_pair):

            if answer == 'x':
                break
            for key in twisted_pair:
                i += 1
                print(f"\n{key}")
                answer = input('> ').lower()
                value = twisted_pair[key]
                if answer == 'x':
                    break
                elif answer == value:
                    print("CORRECT")
                else:
                    print(f"Not Quite: {value}")
                    wrong_standard.append(key)
                    wrong_standard.append(value)
        print("===========")
        print("Twisted Pair Standards missed")
        print(wrong_standard)
        print()
        mod5_menu()
        response = input('> ')
        if response == '1':
            ethernet_cable_standards()
        elif response == '2':
            ethernet_fiber_standards()
        elif response == '3':
            twisted_pair_standards()
        elif response == '4':
            pin_outs_T568A()
        elif response == '5':
            pin_outs_T568B()
        elif response == '6':
            cabling_terms()
        else:
            print("Back to main menu")

    else:
        print("Back to main menu")


def pin_outs_T568A():
    """Function to train on T568-A pin out colored wires"""

    T568A = {'T568A-1': 'white/green', 'T568A-2': 'green',
             'T568A-3': 'white/orange', 'T568A-4': 'blue',
             'T568A-5': 'white/blue', 'T568A-6': 'orange',
             'T568A-7': 'white/brown', 'T568A-8': 'brown'}

    print("Train on T568-A pin out colored wires | (x) to exit")
    i = 0
    answer = ""
    wrong_pinouts = []
    while i < len(T568A):
        for key in T568A:
            i += 1
            print(f"\n{key}")
            answer = input('> ').lower()
            value = T568A[key]
            if answer == 'x':
                print("Goodbye")
                break
            elif answer == value:
                print("CORRECT")
            else:
                print(f"Not Quite: {value}")
                wrong_pinouts.append(key)
                wrong_pinouts.append(value)
    print("==========")
    print("T568-A colored wires missed")
    print(wrong_pinouts)
    print()
    mod5_menu()
    response = input('> ')
    if response == '1':
        ethernet_cable_standards()
    elif response == '2':
        ethernet_fiber_standards()
    elif response == '3':
        twisted_pair_standards()
    elif response == '4':
        pin_outs_T568A()
    elif response == '5':
        pin_outs_T568B()
    elif response == '6':
        cabling_terms()
    else:
        print("Back to main menu")


def pin_outs_T568B():
    """Function to train on T568-B pin out colored wires"""

    T568B = {'T568B-1': 'white/orange', 'T568B-2': 'orange',
             'T568B-3': 'white/green', 'T568B-4': 'blue',
             'T568B-5': 'white/blue', 'T568B-6': 'green',
             'T568B-7': 'white/brown', 'T568B-8': 'brown'}

    print("Train on T568-B pin out colored wires | (x) to exit")
    i = 0
    answer = ""
    wrong_pinouts = []
    while i < len(T568B):
        for key in T568B:
            i += 1
            print(f"\n{key}")
            answer = input('> ').lower()
            value = T568B[key]
            if answer == 'x':
                print("Goodbye")
                break
            elif answer == value:
                print("CORRECT")
            else:
                print(f"Not Quite: {value}")
                wrong_pinouts.append(key)
                wrong_pinouts.append(value)
    print("==========")
    print("T568-B colored wires missed")
    print(wrong_pinouts)
    print()
    mod5_menu()
    response = input('> ')
    if response == '1':
        ethernet_cable_standards()
    elif response == '2':
        ethernet_fiber_standards()
    elif response == '3':
        twisted_pair_standards()
    elif response == '4':
        pin_outs_T568A()
    elif response == '5':
        pin_outs_T568B()
    elif response == '6':
        cabling_terms()
    else:
        print("Back to main menu")


def cabling_terms():
    """Function to train on Module 5 terms and definitions"""
    mod5_terms_dict = {}
    with open('/home/mitchell/Code/projects/networking/networking_pkg/mod5_cabling.txt', 'r') as m:
        lines = m.readlines()

    for line in lines:
        key, value = line.split(':')
        value = value.strip()
        mod5_terms_dict[key] = value

    print("Train on Module 5 Terms and Definitions (Y) | (x) to exit")
    response = input('> ').lower()
    if response == 'y':
        print("==== LET'S TRAIN ====")

        i = 0
        answer = ""
        wrong_answer = []
        while i < len(mod5_terms_dict):
            if answer == 'x':
                break
            for key in mod5_terms_dict:
                i += 1
                print(key)
                value = mod5_terms_dict[key]
                answer = input('> ').lower()
                if answer == 'x':
                    break
                elif answer == value.lower():
                    print("CORRECT\n")
                else:
                    print("Not Quite")
                    print(value)
                    wrong_answer.append(key)
                    wrong_answer.append(value)
        print("==========")
        print("Terms to work on")
        print(wrong_answer)
    else:
        print("BACK TO MAIN MENU")
