import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD99 = 998244353

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())
EI = lambda m: [NLI() for _ in range(m)]


def f(X: str):
    ans = 0
    D = len(X)
    x0 = int(X[0])
    over = False
    for i, x in enumerate(X):
        x = int(x)
        for y in range(1, x):
            ans += pow(y-1, D-1-i)

        if not over:
            for y in range(x0):
                if y == 0:
                    ans += 1
                elif y < x:
                    ans += pow(y, D-1-i)
                else:
                    break
            if x >= x0:
                over = True
    return ans

def main():
    for X in range(10, 300):
        print(X, f(str(X)))


    L, R = SMI()
    print(f(R) - f(str(int(L)-1)))


if __name__ == "__main__":
    main()
