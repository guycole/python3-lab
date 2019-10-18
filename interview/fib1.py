#
# Title:fib1.py
# Description: fib sequence
# Development Environment:Ubuntu 18.04.3 LTS (Bionic Beaver)/Python 3.6.8
# Legalise:Copyright (C) 2019 Miserable Bastards, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#

def fib2(n):
    yield 0
    if n > 0: yield 1
    last = 0
    next = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next

def fib(n):
    if n == 0:
        return n
    last = 0
    next2 = 1
    for _ in range (1, n):
        last, next2 = next2, last + next2
    return next2

print("start")
print(fib(7))
