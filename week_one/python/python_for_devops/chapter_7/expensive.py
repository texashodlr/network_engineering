import logging

def expensive_operation():
    word = "Banana"
    num  = 4

    return (word + num + word)

def test():
    print("Running Expensive Operation\n")
    try:
        return expensive_operation()
    except TypeError:
        logging.exception("Running expensive_operation caused error")

test()
