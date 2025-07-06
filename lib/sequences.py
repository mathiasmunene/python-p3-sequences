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
    fib_list = [0, 1]
    while len(fib_list) < length:
        fib_list.append(fib_list[-1] + fib_list[-2])
    print(fib_list)


# def fibonacci(n):
#     if n <= 0:
#         return []
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]
#     else:
#         seq = fibonacci(n-1)
#         seq.append(seq[-1] + seq[-2])
#         return seq