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
    ans = 0
    P2H = [i for i in range(N)]
    C = [1] * N
    for _ in range(Q):
        qi, *X = NMI()
        if qi == 1:
            p, h = X
            p -= 1
            h -= 1
            h0 = P2H[p]
            P2H[p] = h
            C[h0] -= 1
            C[h] += 1
            if C[h0] == 1:
                ans -= 1
            if C[h] == 2:
                ans += 1
        else:
            print(ans)


if __name__ == "__main__":
    main()
