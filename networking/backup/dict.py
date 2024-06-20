#!/usr/bin/python3

dictionary = {20: 'ftp', 21: 'ftp', 22: 'ssh', 23: 'telnet', 25: 'smtp',
              67: 'dhcp', 68: 'dhcp', 69: 'tftp', 80: 'http', 110: 'pop3',
              123: 'ntp', 161: 'snmp', 162: 'snmp', 389: 'ldap', 443: 'https',
              445: 'smb', 514: 'syslog', 587: 'smtps', 636: 'ldaps',
              1433: 'sql', 3389: 'rdp', 5060: 'sip', 5061: 'sip'}

print(len(dictionary))

for i in range(len(dictionary)):
    i += 1
    print(i)

