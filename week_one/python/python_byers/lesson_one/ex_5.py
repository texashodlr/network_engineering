#!/usr/bin/env python3

ip_addr = "10.12.17.1"
mac_addr = "0024.c4e9.48ae"

print("String concatenation:\n "+ip_addr+" --> "+mac_addr+" ")

print(f"f-String concatenation:\n {ip_addr} --> {mac_addr}")

print("format() method: \n {} --> {}".format(ip_addr, mac_addr))
