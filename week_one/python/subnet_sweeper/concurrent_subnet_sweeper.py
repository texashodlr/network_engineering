#!/usr/bin/env python3

# This script is a concurrent version of the other subnet sweeper allowing users to concurrently ping multiple subnets
# This script builds on ip scanner and checks whole subnets
# Pulled from: https://www.packetswitch.co.uk/how-to-ping-sweep-your-network-with-python/

import datetime
import ipaddress
import concurrent.futures
import threading
import csv
from ping3 import ping

subnets = ['192.168.1.0/29', '192.168.60.0/29', '192.168.69.0/29']
output_file = 'subnet_sweep_results.csv'
output_lock = threading.Lock()

def ping_sweep(subnet):
    network = ipaddress.ip_network(subnet, strict=False)
    results = []

    for ip in network.hosts():
        ip_str = str(ip)
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            response_time = ping(ip_str, timeout=1)
            if response_time is not None:
                message = f"{timestamp} - {ip_str} is reachable"
            else:
                message = f"{timestamp} - {ip_str} is unreachable"
        except Exception:
            message = f"{timestamp} - Error pinging {ip_str}"
        
        results.append(message)

    with output_lock:
        print(f"Ping results for subnet {subnet}:")
        with open (output_file, 'a') as f:
            f.write(f"Ping results for subnet {subnet}:\n")
            for msg in results:
                print(msg)
                f.write(msg + '\n')
            f.write('\n')
        print()

with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(ping_sweep, subnets)
