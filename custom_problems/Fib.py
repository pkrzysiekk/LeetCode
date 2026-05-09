import sys
cache = dict()


def Fib(n):
    if n in cache:
        return cache[n]
    if n <= 2:
        return 1
    res = Fib(n - 1) + Fib(n - 2)
    cache[n] = res
    return res


sys.setrecursionlimit(10**9)
print(Fib(18))
