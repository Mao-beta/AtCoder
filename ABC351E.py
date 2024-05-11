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
    N = NI()
    XY = EI(N)
    odds = []
    evens = []
    for x, y in XY:
        if (x+y) % 2:
            odds.append([(x+y)//2, (x-y)//2])
        else:
            evens.append([(x+y)//2, (x-y)//2])

    def solve(P):
        X = [x for x, _ in P]
        Y = [y for _, y in P]

        def _solve(L):
            res = 0
            L.sort()
            for i in range(len(L)-1):
                g = L[i+1] - L[i]
                res += g * (i+1) * (len(L)-1-i)
            return res

        return _solve(X) + _solve(Y)

    print(solve(odds) + solve(evens))



if __name__ == "__main__":
    main()
