#!/usr/bin/env python3

ips = ['192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4', '192.168.1.5']

print("5 IPs coming at ya hot n ready!\n")
for ip in ips:
    print(f"{ip}\n")

print(f"Appending an IP: {ips.append('192.168.1.6')}\n")

print(f"Extending IPs: {ips.extend(['192.168.1.7','192.168.1.8'])}\n")

print("8 IPs coming at ya hot n ready!\n")
for ip in ips:
    print(f"{ip}\n")

print(f"The first IP is: {ips[0]}\n")
print(f"The last IP is: {ips[len(ips)-1]}\n")
print("Popping!")
print(f"First address: {ips.pop(0)}\n")
print(f"Last address: {ips.pop()}\n")
print("Pushing!")
ips = ['2.2.2.2'] + ips
print(f"New first IP is: {ips[0]}\n")
