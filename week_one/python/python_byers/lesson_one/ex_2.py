#!/usr/bin/env python3

data_center_location = input("Where is your data center located?")

print(f"Upper Case: \n{data_center_location.upper()}")

print(f"Strip off whitespace: \n Original: {data_center_location} \n Stripped: {data_center_location.strip()}")

print(f"Method chaining: \n {data_center_location.strip().upper()}")
