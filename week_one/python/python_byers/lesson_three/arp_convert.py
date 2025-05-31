filename = "junos_show_arp.txt"

arp_list = []

with open(filename) as f:
    ip_intf = f.readlines()

for i in range(len(ip_intf)-1):
    if ":" in ip_intf[i]:
        temp = ip_intf[i].split()
        t = (temp[0]).replace(":","-")
        arp_list.append(t)

print("\n\n")
for i in range(len(arp_list)):
    print(f"ARP List: {arp_list[i]}\n")
