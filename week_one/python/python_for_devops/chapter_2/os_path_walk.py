#!/usr/bin/env python3


import fire
import os

def walk_path(parent_path):
    print(f"Checking: {parent_path}")
    childs = os.listdir(parent_path)

    for child in childs:
        child_path = os.path.join(parent_path,child)
        if os.path.isfile(child_path):
            last_access = os.path.getatime(child_path)
            size = os.path.getsize(child_path)
            print(f"File: {child_path}")
            print(f"\tLast Accessed: {last_accessed}")
            print(f"\tSize: {size}")
        elif os.path.isdir(child_path):
            walk_path(child_path)

if __name__ == '__main__':
    fire.Fire()


