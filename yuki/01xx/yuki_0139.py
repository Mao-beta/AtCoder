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
    N, L = NMI()
    XWT = EI(N)
    now = 0
    ans = 0
    for x, w, t in XWT:
        if now < x:
            ans += x - now
            now = x
        if ans % (2*t) > t-w:
            ans = (ans + 2*t-1) // (2*t) * (2*t)
        ans += w
        now += w
    ans += L - now
    print(ans)


if __name__ == "__main__":
    main()
