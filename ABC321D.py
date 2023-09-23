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
    N, M, P = NMI()
    A = sorted(NLI())
    B = sorted(NLI())
    CB = list(accumulate([0]+B))

    ans = 0
    for a in A:
        r = P - a
        k = bisect.bisect_right(B, r)
        ans += CB[k] + a * k + P * (M-k)

    print(ans)


if __name__ == "__main__":
    main()
