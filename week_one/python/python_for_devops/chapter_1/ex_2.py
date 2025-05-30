#!/usr/bin/env python3

def isUpper(phrase):
    print(f"The String is: ")
    if phrase == phrase.upper():
        print("uppercase!")
    elif phrase == phrase.lower():
        print("lowercase!")
    else:
        print("neither!")

phrase = input("Please enter a lower or upper case (preferably only) string: ")
isUpper(phrase)

