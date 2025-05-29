#!/usr/bin/env python3

file = open("show_version.txt")

data = file.read()
file.close()

print(f"The first line is: \n{data.splitlines()[0]}\n")
print(f"Data is of type: {type(data)}\n")
print("Closing the file...\n")
print("\nPart 2!\n")
with open("show_version.txt", mode='r') as f:
    data = f.readlines()

print(f"The first line is: \n{data[0].strip()}\n")
print(f"Data is of type: {type(data)}\n")
