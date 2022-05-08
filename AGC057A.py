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
    T = NI()
    for _ in range(T):
        L, R = SMI()

        if len(L) == len(R):
            print(int(R) - int(L) + 1)

        elif R[0] != "1":
            base = 10 ** (len(R) - 1)
            print(int(R) - base + 1)

        else:
            base = 10 ** (len(R) - 1)
            ans = int(R) - base + 1
            rl = int(R[:-1])
            rr = int(R[1:])
            r = max(rl, rr)

            ll = max(10 ** (len(R) - 2), int(L))
            ll = max(r+1, ll)
            lr = base - 1
            print(ans + max(0, lr - ll + 1))


if __name__ == "__main__":
    main()
