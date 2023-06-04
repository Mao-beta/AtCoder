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
    N, V = NMI()
    A = NLI()
    B = NLI()
    C = NLI()
    D = NLI()
    AB = Counter()
    for a in A:
        for b in B:
            AB[a+b] += 1

    CD = Counter()
    for c in C:
        for d in D:
            CD[c+d] += 1

    ans = 0
    for x, k in AB.items():
        ans += CD[V-x] * k

    print(ans)


if __name__ == "__main__":
    main()
