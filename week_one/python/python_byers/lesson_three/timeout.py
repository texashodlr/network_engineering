import time

# This script should stay in a while loop until a timeout expires.

def time_burning(time_limit):
    # time_limit is denominated in seconds
    print(f"Timeout initiating for {time_limit} seconds...\n\n")
    start_time = int(time.time())
    end_time = start_time+time_limit
    while start_time < end_time:
        current_time = int(time.time())
        if current_time >= end_time:
            print("\n\n\t\t\tLimit reached!\n\n")
            print(f"Start time: {start_time} \t\t Current time: {current_time} \t\t End time: {end_time}\n")
            break
        time.sleep(1)
        print(f"Start time: {start_time} \t\t Current time: {current_time} \t\t End time: {end_time}\n")


time_limit = int(input("\t\t\t Welcome!\nHow much time shall we burn? "))
time_burning(time_limit)
