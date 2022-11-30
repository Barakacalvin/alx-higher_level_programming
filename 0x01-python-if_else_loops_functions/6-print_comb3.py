#!/usr/bin/python3
for no in range(0, 10):
    for num in range((no+1), 10):
        if (no != 8) or (num != 9):
            print("{}{}, ".format(no, num), end="")
        else:
            print("{}{}".format(no, num))
