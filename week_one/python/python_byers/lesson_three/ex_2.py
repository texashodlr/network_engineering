file_name = "show_ip_int_brief.txt"

with open(file_name) as f:
    txt_line = f.readlines()
for l in txt_line:
    #print(f"Line: {l}\n")
    if "10.220" in l:
        new_line = l.split()
        intf_name = new_line[0]
        ip_addr   = new_line[1]
        print(f"Interface Name: {intf_name}\n")
        print(f"IP Address    : {ip_addr}\n")

print("Completed.\n")
