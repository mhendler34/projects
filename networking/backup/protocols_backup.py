#!/usr/bin/python3
# Python Training Program to help with Network Ports and Protocols

# Dictionary to hold ports (keys) and protocols (values)
dictionary = {20: 'ftp-data', 21: 'ftp-control', 22: 'ssh', 23: 'telnet',
              25: 'smtp', 67: 'dhcp-client', 68: 'dhcp-server', 69: 'tftp',
              80: 'http', 110: 'pop3', 123: 'ntp', 143: 'imap4', 161: 'snmp',
              162: 'snmp', 389: 'ldap', 443: 'https', 445: 'smb',
              514: 'syslog', 587: 'smtp-tls', 636: 'ldaps', 993: 'imap4-ssl',
              995: 'pop3-ssl', 1433: 'sql', 1521: 'sqlnet', 3306: 'mysql',
              3389: 'rdp', 5060: 'sip', 5061: 'sip'}

# Turn this into a function at some point

print("Would you like to train on network ports and their protocols today?")
print("Enter (Y) | (n)")
response = input('> ').lower()

if response == 'y':
    print("Let's train")
    print("Type in the protocol associated with the port number")
    #  Call Function Here

    wrong_protocols = []  # List of protocols missed
    right_protocols = []  # List of protocols correct

    i = 0
    while i < len(dictionary):
        #  Loops through keys by default
        for port in dictionary:
            i += 1
            print(f"\n{port}")
            answer = input('> ').lower()
            protocol = dictionary[port]
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
    # train again, call function again here'

    #  for wrong in wrong_protocols:
    #    print(wrong)

else:
    print("Maybe tomorrow")
