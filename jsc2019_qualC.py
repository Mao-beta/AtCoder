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
    N = NI()
    S = SI()
    S = [int(s == "B") for s in S]
    now = 0
    ans = 1
    for s in S:
        if s and now % 2:
            ans = ans * now % MOD
            now -= 1
        elif s:
            now += 1
        elif now % 2:
            now += 1
        else:
            ans = ans * now % MOD
            now -= 1

    if now != 0:
        print(0)
        exit()

    for i in range(1, N+1):
        ans = ans * i % MOD

    print(ans)


if __name__ == "__main__":
    main()
