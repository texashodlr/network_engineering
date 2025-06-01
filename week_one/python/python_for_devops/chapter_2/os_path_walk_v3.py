import os

def walk_path(parent_path):
    for parent_path, directories, files in os.walk(parent_path):
        print(f"Checking: {parent_path}")
        for file_name in files:
            file_path = os.path.join(parent_path, file_name)
            last_access = os.path.getatime(file_path)
            size = os.path.getsize(file_path)
            print(f"File: {file_path}")
            print(f"\tLast Accessed: {last_access}")
            print(f"\tSize: {size}")

parent_path = input("Enter the path that shall be walked: ")
walk_path(parent_path)
