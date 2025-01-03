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
    A, B, X = NMI()

    if X >= A * 10**9 + B:
        print(10**9)
        exit()

    k = 10**8
    ans = 0
    while X > 0 and k > 0:
        d = 0
        for i in range(10):
            if X >= (A * k + B) * i:
                d = i
        X -= (A * k + B) * d
        ans += d * k
        k //= 10

    print(ans)


if __name__ == "__main__":
    main()
