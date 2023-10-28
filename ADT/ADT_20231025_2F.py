import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
    N = NI()
    ans = 0
    for K in range(1, 19):
        if N >= 10**K:
            num = 9 * 10**(K-1)
            ans += (num+1) * num // 2
        else:
            num = N - 10**(K-1) + 1
            ans += (num+1) * num // 2
            break
    print(ans % MOD99)


if __name__ == "__main__":
    main()
