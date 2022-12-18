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
    S = [SI() for _ in range(10)]
    a, b, c, d = 0, 0, 0, 0
    for i in range(10):
        for j in range(10):
            if S[i][j] == "#":
                a = i+1
                c = j+1
                break
        if a > 0:
            break

    for i in range(9, -1, -1):
        for j in range(9, -1, -1):
            if S[i][j] == "#":
                b = i+1
                d = j+1
                break
        if b > 0:
            break

    print(a, b)
    print(c, d)


if __name__ == "__main__":
    main()
