#!/usr/bin/env python3

# This script is designed to iterate through and ip range, pinging every single IP to determine if there's an IP there.

from ping3 import ping

import ipaddress

a = ping('8.8.8.8')
b = ping('192.168.1.57')

print(a)
print(b)


# Network is a subnet object
# Use a for-loop to print all ip-addr vals
network = ipaddress.ip_network('192.168.1.0/24')
for ip in network:
        print(ip)
        
