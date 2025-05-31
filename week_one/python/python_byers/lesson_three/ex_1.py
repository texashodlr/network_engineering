base_addr  = "192.168.254."
prefix_len = int(input("Please enter a prefix length between 25-30: "))

subnet_size  = 32 - prefix_len
subnet_count = int(256 / (2**subnet_size))


print()
print("Subnets:\n")
print(f"\tNumber of hosts in the subnet: {((2**subnet_size)-2)}\n")
print(f"\tNumber of Subnets: {subnet_count}\n")
for i in range(subnet_count):
    # print("\t\tSubnet Number: {base_addr}{(1-i)+(2**subnet_size)}\n")
    print(f"\t\tSubnet Number: {base_addr}{(i*(2**subnet_size))}\n")
print(f"\tFirst Host Addr: {base_addr}1\n")
print(f"\tLast Host Addr: {base_addr}{(2**subnet_size)-2}\n")
