#!/usr/bin/env python3

def print_fibonacci(length):
    fib_list = []
    if length <= 0:
        print(fib_list)
        return
    elif length == 1:
        fib_list = [0]
        print(fib_list)
        return