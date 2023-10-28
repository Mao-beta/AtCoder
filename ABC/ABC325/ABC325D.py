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
    TD = EI(N)
    hq = []
    T2L = defaultdict(list)
    Ts = set()
    for t, d in TD:
        Ts.add(t)
        T2L[t].append(t+d)

    Ts = sorted(list(Ts))
    Ts.append(10**19)
    ans = 0
    for i, t in enumerate(Ts[:-1]):
        now = t
        while hq and hq[0] < now:
            heappop(hq)

        for l in T2L[t]:
            heappush(hq, l)

        while hq and now < Ts[i+1]:
            heappop(hq)
            ans += 1
            now += 1

            while hq and hq[0] < now:
                heappop(hq)

    print(ans)


if __name__ == "__main__":
    main()
