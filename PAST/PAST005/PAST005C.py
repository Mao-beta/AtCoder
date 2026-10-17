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

    if N == 0:
        print(0)
        exit()

    ans = ""

    S = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    while N > 0:
        x = N % 36
        ans = S[x] + ans
        N //= 36

    print(ans)


if __name__ == "__main__":
    main()
