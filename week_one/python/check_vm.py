#!/usr/bin/env python3
import paramiko

# This script is a simple ssh script to log into a VM and perform a 'top' check
# Host
host = input("Host IP: \n")

# User
username = input("Username: \n")

# Pw
password = input("password:\n")

# Creating a SSH Client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to a remote host
client.connect(host, username=username, password=password)

# Executes a 'top' snapshot on the respective machine
stdin, stdout, stderr = client.exec_command("top -b -n 1")
print(stdout.read().decode())

# Close the connection
client.close();
