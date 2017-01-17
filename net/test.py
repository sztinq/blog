__author__ = 'tinq'

line = ['dis', 'arp', '|', 'in', '192.168.141.103', 'Type:', 'S-Static', 'D-Dynamic', 'IP', 'Address', 'MAC', 'Address',
        'VLAN', 'ID', 'Interface', 'Aging', 'Type', '192.168.141.103', '507b-9da8-dde1', '501', 'GE1/0/9', '20', 'D',
        '<F5-AGG>']
line2 = line[17:]
for i in range(len(line2)):
        print i
        print line2[i]