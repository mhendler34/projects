#!/usr/bin/python3

from networking_pkg import flashcards_function


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


def ethernet_cable_standards():
    """FUNCTION to train on ethernet cable standards and their metrics"""

    subject = "ethernet cable standards"
    dictionary = {'10BASE-T-Mbps': '10mbps', '10BASE-T-dist': '100m',
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

    flashcards_function.flash_cards(subject, dictionary)  # Training program
    mod5_menu()


def ethernet_fiber_standards():
    """Function to train on ethernet Fiber Optic standards"""

    subject = "ethernet fiber standards"
    dictionary = {'100BASE-SX-Mbps': '100mbps', '100BASE-SX-dist': '300m',
                  '100BASE-SX-media': 'mmf', '100BASE-FX-Mbps': '100mbps',
                  '100BASE-FX-dist': '2000m', '100BASE-FX-media': 'mmf',
                  '1000BASE-SX-Mbps': '1000mbps', '1000BASE-SX-dist': '550m',
                  '1000BASE-LX-Mbps': '1000mbps', '1000BASE-LX-dist-mmf':
                  '550m', '1000BASE-LX-dist-smf': '5000m',
                  '1000BASE-LX-media': 'mmf/smf', '10GBASE-SR-Mbps': '10000mbps',
                  '10GBASE-SR-dist': '300m', '10GBASE-SR-media': 'mmf',
                  '10GBASE-LR-Mbps': '10000mbps', '10GBASE-LR-dist': '10000m',
                  '10GBASE-LR-media': 'smf'}
    flashcards_function.flash_cards(subject, dictionary)
    mod5_menu()


def twisted_pair_standards():
    """Function to train on twisted pair category standards"""

    subject = "twisted pair standards"
    dictionary = {'cat3-mbps': '10mbps', 'cat5-mbps': '100mbps',
                  'cat5e-mbps': '1000mbps', 'cat6-mbps': '1gbps/10gbps',
                  'cat6a-mbps': '10gbps', 'cat7-mbps': '10gbps/100gbps',
                  'cat8-mbps': '25gbps/40gbps'}
    flashcards_function.flash_cards(subject, dictionary)
    mod5_menu()


def pin_outs_T568A():
    """Function to train on T568-A pin out colored wires"""

    subject = "T568A pin out colored wires"
    dictionary = {'T568A-1': 'white/green', 'T568A-2': 'green',
                  'T568A-3': 'white/orange', 'T568A-4': 'blue',
                  'T568A-5': 'white/blue', 'T568A-6': 'orange',
                  'T568A-7': 'white/brown', 'T568A-8': 'brown'}
    flashcards_function.flash_cards(subject, dictionary)
    mod5_menu()


def pin_outs_T568B():
    """Function to train on T568-B pin out colored wires"""

    subject = "T568B pin out colored wires"
    dictionary = {'T568B-1': 'white/orange', 'T568B-2': 'orange',
                  'T568B-3': 'white/green', 'T568B-4': 'blue',
                  'T568B-5': 'white/blue', 'T568B-6': 'green',
                  'T568B-7': 'white/brown', 'T568B-8': 'brown'}
    flashcards_function.flash_cards(subject, dictionary)
    mod5_menu()


def cabling_terms():
    """Function to train on Module 5 terms and definitions"""
    mod5_terms_dict = {}
    with open('/home/mitchell/Code/projects/networking/networking_pkg/mod5_cabling.txt', 'r') as m:
        lines = m.readlines()

    for line in lines:
        key, value = line.split(':')
        value = value.strip()
        mod5_terms_dict[key] = value

    subject = "module 5 terms and definitions"
    dictionary = mod5_terms_dict
    flashcards_function.flash_cards(subject, dictionary)
    mod5_menu()
