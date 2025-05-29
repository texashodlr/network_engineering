#!/usr/bin/env python3
from rich import print

base_addr = "192.168.254."

prefix_len = int(input("Please choose a prefix length between 25-30: "))

subnet_size = 2**(32-prefix_len)
host_count = subnet_size - 2

net_num_a = f"{base_addr}0"
net_num_b = f"{base_addr}{subnet_size}"
first_host_addr = f"{base_addr}1"
last_host_addr = f"{base_addr}{host_count}"

print("\n---Results---")
print(f"Number of hosts on the subnet: {host_count}\n")
print(f"First & Second Subnets: {net_num_a} & \n\t\t\t{net_num_b}\n")
print(f"First Subnet: {net_num_a}\n")
print(f"First Host address: {first_host_addr}\n")
print(f"Last Host address:  {last_host_addr}\n")
