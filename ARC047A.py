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
    N, L = NMI()
    S = SI()
    now = 1
    ans = 0
    for s in S:
        if s == "+":
            now += 1
        else:
            now -= 1
        if now > L:
            ans += 1
            now = 1
    print(ans)


if __name__ == "__main__":
    main()
