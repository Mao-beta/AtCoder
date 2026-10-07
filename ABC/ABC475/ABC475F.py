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
    H, W = NMI()
    S = [list(SI()) for _ in range(H)]
    if H > W:
        S = [list(a) for a in zip(*S)]
        H, W = W, H

    # 行hにおける最も右の"."
    Wmax = [0] * H
    for h in range(H):
        for w in range(W):
            if S[h][w] == ".":
                Wmax[h] = w

    ans = 1
    for u in range(H):
        # [u, d)で"."があるか
        A = [0] * W
        # Aの累積和
        C = [0] * (W+1)
        for d in range(u+1, H+1):
            C[0] = 0
            umax, dmax = -1, -1
            for r in range(1, W+1):
                if S[d-1][r-1] == ".":
                    A[r-1] = 1
                    dmax = r-1
                if S[u][r-1] == ".":
                    umax = r-1
                C[r] = C[r-1] + A[r-1]
                lmax = min(umax, dmax)
                if A[r-1]:
                    ans += C[lmax+1]
    print(ans)



if __name__ == "__main__":
    main()
