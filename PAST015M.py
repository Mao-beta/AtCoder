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
    D = NLI()
    x = 1
    for d in D:
        x |= x << (2*d)
    S = sum(D)
    ans = S
    for i in range(S):
        if (x >> (S+i)) & 1:
            ans = min(ans, i)
            break
        if (x >> (S-i)) & 1:
            ans = min(ans, i)
            break
    print(ans)


if __name__ == "__main__":
    main()
