def print_numbers(lowest, highest):
    print("== Job processing started")
    x = lowest
    while x <= highest:
        print("{}\n".format(x)) 
        x += 1
    print("== Job processing finished")