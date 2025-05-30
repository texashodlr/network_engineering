#!/usr/bin/env python3

with open("show_arp.txt") as f:
    show_arp = f.readlines()

print()
print(f"Python Data type of show_arp: {type(show_arp)}\n")
print(f"             Len of show_arp: {len(show_arp)}\n")
print(f"     Header line of show_arp: {show_arp[0]}\n")
print(f" First data line of show_arp: {show_arp[1]}\n")
print(f" First data line of show_arp: {show_arp[-1]}\n")
fields = show_arp[0].split()

print(f"Fields variable: {fields}\n")
print(f"Python data type of fields: {type(fields)}\n")
print(f"Number of entries in fields: {len(fields)}\n")
print(f"First field: {fields[0]}\n")
print(f"Last field:  {fields[-1]}\n")

fields.pop(3)
temp = fields.pop(4)
print(f"Correcting hardware_addr: {temp}\n")
fields[3] = fields[3] + "_" + temp
print(f"Corrected fields: {fields}\n")

