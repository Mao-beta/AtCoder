import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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
    N, Q = NMI()
    X2LR = [[] for _ in range(Q)]
    for _ in range(Q):
        l, r, x = NMI()
        X2LR[x-1].append([l-1, r])
    imos = [0] * (N+2)
    for x in range(Q):
        X2LR[x].sort()
        X2LR[x].append([N+1, N+1])
        # print(x, X2LR[x])
        nl = 0
        nr = 0
        for l, r in X2LR[x]:
            if nr < l:
                imos[nl] += 1
                imos[nr] -= 1
                # print(nl, nr)
                nl, nr = l, r

            else:
                nr = max(nr, r)
    ans = list(accumulate(imos))
    print(*ans[:-2])


if __name__ == "__main__":
    main()
