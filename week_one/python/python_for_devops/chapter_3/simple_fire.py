#!/usr/bin/env python3
"""
Simple command line tool using fire
"""
import fire

def greet(greeting = 'Hiya', name = 'Tammy'):
    print(f"{greeting} {name}")

if __name__ == '__main__':
    fire.Fire(greet)
