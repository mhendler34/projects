#!/usr/bin/python3

from networking_pkg import flashcards_function


def get_protocols():
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
    print("\nTrain again? (Y) to begin | (x) to exit")
    response = input('> ').lower()
    if response == 'y':
        get_protocols()
    else:
        print("BACK TO MAIN MENU")
