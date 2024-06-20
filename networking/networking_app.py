#!/usr/bin/python3
# Networking Training Program

from networking_pkg import contents, protocols, conversion, mod5_cabling


while True:
    contents.main_menu()
    response = input('> ')
    if response == '1':
        protocols.get_protocols()  # protocols module, get_protocols function
    elif response == '2':
        conversion.bin_dec()  # binary module, bin_dec function
    elif response == '3':
        conversion.bin_hex()
    elif response == '4':
        conversion.hex_dec()
    elif response == '5':
        mod5_cabling.mod5_menu()
        user_choice = input('> ')
        if user_choice == '1':
            mod5_cabling.ethernet_cable_standards()
        elif user_choice == '2':
            mod5_cabling.ethernet_fiber_standards()
        elif user_choice == '3':
            mod5_cabling.twisted_pair_standards()
        elif user_choice == '4':
            mod5_cabling.pin_outs_T568A()
        elif user_choice == '5':
            mod5_cabling.pin_outs_T568B()
        elif user_choice == '6':
            mod5_cabling.cabling_terms()
        else:
            print("\nBACK TO MAIN MENU")
            continue
    elif response == '6':
        print("TODO: TCP Segment Headers")
    else:
        print("Maybe tomorrow")
        break
