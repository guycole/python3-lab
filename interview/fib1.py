#
# Title:fib1.py
# Description: fib sequence
#
memo = {0:0, 1:1}

def fib4(n):
    if n not in memo:
        memo[n] = fib4(n-1) + fib4(n-2)
    return memo[n]

#def fib3(n):
#    yield 0
#    if n > 0: yield 1
#    last = 0
#    next = 1
#    for _ in range(1, n):
#        last, next = next, last + next
#        yield next

def fib2(n):
    if n == 0:
        return n
    last = 0
    next2 = 1
    for _ in range (1, n):
        last, next2 = next2, last + next2
    return next2

def fib1(n):
    if n < 2:
        return n
    return fib1(n-2) + fib1(n-1)

print("start")
print(fib1(7))
