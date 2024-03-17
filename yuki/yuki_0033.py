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
    N, D, T = NMI()
    X = NLI()
    Y = defaultdict(list)
    for x in X:
        Y[x%D].append(x)
    ans = 0
    for k in Y.keys():
        Y[k].sort()
        L = []
        for x in Y[k]:
            l = x - D * T
            r = x + D * T
            if len(L) == 0:
                L.append([l, r])
            else:
                lp, rp = L[-1]
                if l <= rp:
                    l = min(lp, l)
                    r = max(rp, r)
                    L.pop()

                L.append([l, r])
        for l, r in L:
            ans += (r-l) // D + 1
    print(ans)



if __name__ == "__main__":
    main()
