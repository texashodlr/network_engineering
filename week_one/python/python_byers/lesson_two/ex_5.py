#!/usr/bin/env python3

intf = "GigabitEthernet1       10.0.2.15       YES DHCP   up                    up"
intf_fields   = intf.split()
intf_name     = intf_fields[0] 
intf_ip_addr  = intf_fields[1]
intf_status   = intf_fields[-1]
intf_protocol = intf_fields[-2]
print(f"Intf     Name: {intf_name}\n")
print(f"Intf  IP_addr: {intf_ip_addr}\n")
print(f"Intf   Status: {intf_status}\n")
print(f"Intf Protocol: {intf_protocol}\n")

line_status = intf_status == intf_protocol == "up"

print(f"Line and protocol status: {line_status}\n")
