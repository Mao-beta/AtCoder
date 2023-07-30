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
    N, M = NMI()
    TX = EI(N)
    hq = []
    cans = []
    openers = []
    hq_sum = 0
    for t, x in TX:
        if t == 0:
            heappush(hq, x)
            hq_sum += x
        elif t == 1:
            cans.append(x)
        else:
            openers.append(x)

    while len(hq) > M:
        x = heappop(hq)
        hq_sum -= x
    cans.sort()
    openers.sort(reverse=True)

    used_opener = 0
    openable = 0

    ans = hq_sum

    for opener in openers:
        openable += opener
        used_opener += 1
        while openable > 0 and cans:
            x = cans.pop()
            heappush(hq, x)
            hq_sum += x
            openable -= 1

        while hq and len(hq) + used_opener > M:
            x = heappop(hq)
            hq_sum -= x

        ans = max(ans, hq_sum)

    print(ans)



if __name__ == "__main__":
    main()
