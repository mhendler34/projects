#!/usr/bin/python3

from networking_pkg import flashcards_function


def get_protocols1():
    """Function to train on network ports and protocols"""

    subject = "network ports and protocols"
    dictionary = {20: 'ftp-data', 21: 'ftp-control', 22: 'ssh', 23: 'telnet',
                  25: 'smtp', 67: 'dhcp-client', 68: 'dhcp-server', 69: 'tftp',
                  80: 'http', 110: 'pop3', 123: 'ntp', 143: 'imap4',
                  161: 'snmp', 162: 'snmp', 389: 'ldap', 443: 'https',
                  445: 'smb', 514: 'syslog', 587: 'smtp-tls', 636: 'ldaps',
                  993: 'imap4-ssl', 995: 'pop3-ssl', 1433: 'sql',
                  1521: 'sqlnet', 3306: 'mysql', 3389: 'rdp', 5060: 'sip',
                  5061: 'sip'}

    flashcards_function.flash_cards(subject, dictionary)


# get_protocols1()


def get_protocols():
    """Function to train on network ports and protocols"""

    dictionary = {20: 'ftp-data', 21: 'ftp-control', 22: 'ssh', 23: 'telnet',
                  25: 'smtp', 67: 'dhcp-client', 68: 'dhcp-server', 69: 'tftp',
                  80: 'http', 110: 'pop3', 123: 'ntp', 143: 'imap4',
                  161: 'snmp', 162: 'snmp', 389: 'ldap', 443: 'https',
                  445: 'smb', 514: 'syslog', 587: 'smtp-tls', 636: 'ldaps',
                  993: 'imap4-ssl', 995: 'pop3-ssl', 1433: 'sql',
                  1521: 'sqlnet', 3306: 'mysql', 3389: 'rdp', 5060: 'sip',
                  5061: 'sip'}

    print("Train on network ports and their protocols today?")
    print("Enter (Y) to begin | (x) to exit")
    response = input('> ').lower()

    if response == 'y':
        print("==== LET'S TRAIN ====")
        print("Type in the protocol associated with the port number")

        wrong_protocols = []  # List of protocols missed
        right_protocols = []  # List of protocols correct

        i = 0
        answer = ""
        while i < len(dictionary):
            #  Loops through keys by default
            if answer == 'x':
                break
            for port in dictionary:
                i += 1
                print(f"\n{port}")
                answer = input('> ').lower()
                protocol = dictionary[port]
                if answer == 'x':
                    print("Goodbye")
                    break
                if answer == protocol:
                    print("Yes, you got it!")
                    right_protocols.append(protocol)
                else:
                    print("NEGATRON! Onto the next one")
                    wrong_protocols.append(port)
                    wrong_protocols.append(protocol)
        # Print summary of training session
        print()
        print("Protocols you missed")
        print(wrong_protocols)
        print("Train again on protocols? (Y) | (x)")
        response = input('> ').lower()
        if response == 'y':
            get_protocols()
        else:
            print("Back to main menu")
            # exit() --> exits out of python completely
    else:
        print("Maybe tomorrow")


