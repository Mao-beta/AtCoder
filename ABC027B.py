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
    A = NLI()
    T = sum(A)
    if T % N:
        print(-1)
        exit()

    K = T // N
    now = 0
    ans = 0
    for i, a in enumerate(A, start=1):
        now += a
        if now != K * i:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
