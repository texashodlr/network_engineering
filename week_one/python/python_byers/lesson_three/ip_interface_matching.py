filename = "show_ip_int_brief.txt"

ip_list = []
intf_list = []

with open(filename) as f:
    ip_intf = f.readlines()

for i in range(len(ip_intf)):
    if "10." in ip_intf[i]:
        temp = ip_intf[i].split()
        intf_list.append(temp[0])
        ip_list.append(temp[1])

print("\n\n")
for i in range(len(intf_list)):
    print(f"Interface: {intf_list[i]}\tIP:{ip_list[i]}\n")

