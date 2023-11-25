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
    N = NI()
    SC = EI(N)
    C = Counter()
    hq = []
    for s, c in SC:
        C[s] += c
        heappush(hq, s)

    while hq:
        s = heappop(hq)
        c = C[s]
        if c // 2 > 0:
            if s*2 not in C:
                heappush(hq, s*2)
            C[s * 2] += c // 2
            C[s] -= c // 2 * 2

    ans = 0
    for s, c in C.items():
        ans += c
    print(ans)


if __name__ == "__main__":
    main()
