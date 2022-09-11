import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

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


def main():
    A, B, C = NMI()

    def judge(X):
        return (-A*X + 100) - B*math.sin(C*math.pi*X) > 1e-7

    upper = 0
    lower = 200 / A
    for i in range(50):
        # print(lower, upper)
        X = (upper + lower) / 2
        if judge(X):
            upper = X
        else:
            lower = X

    print(upper)
    # X = upper
    # print(A*X + B*math.sin(C*math.pi*X))


if __name__ == "__main__":
    main()
