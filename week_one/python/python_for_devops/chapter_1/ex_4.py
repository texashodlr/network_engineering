def even_odd(times):
    num = 0
    while num < times:
        if num%2 == 0:
            print(f"Current count: {num}, EVEN!\n")
        else:
            print(f"Current count: {num}, ODD!\n")
        num += 1

times = int(input("What is your desired number of iterations? "))
even_odd(times)
