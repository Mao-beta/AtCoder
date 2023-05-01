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
    N, T = NMI()
    C = NLI()
    R = NLI()
    if T in C:
        ans = 0
        M = 0
        for i, (c, r) in enumerate(zip(C, R), start=1):
            if M < r and c == T:
                ans = i
                M = r

    else:
        ans = 1
        M = R[0]
        for i, (c, r) in enumerate(zip(C, R), start=1):
            if M < r and c == C[0]:
                ans = i
                M = r

    print(ans)


if __name__ == "__main__":
    main()
