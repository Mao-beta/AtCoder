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
EI = lambda m: [NLI() for _ in range(m)]


def main():
    H, W = NMI()
    A = EI(H)
    for h in range(H):
        tmp = []
        for w in range(W):
            a = A[h][w]
            if a == 0:
                tmp.append(".")
            else:
                tmp.append(chr(ord("A") + a - 1))
        print("".join(tmp))


if __name__ == "__main__":
    main()
