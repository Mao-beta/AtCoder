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
    T = NI()
    for _ in range(T):
        N = NI()
        WP = EI(N)
        WP.sort(key=lambda wp: -wp[1]-wp[0])
        W = sum(w for w, p in WP)
        P = 0
        for i, (w, p) in enumerate(WP):
            W -= w
            P += p
            # print(i, w, p, W, P)
            if W <= P:
                print(N - (i+1))
                break


if __name__ == "__main__":
    main()
