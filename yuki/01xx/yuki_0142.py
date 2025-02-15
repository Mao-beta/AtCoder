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
    N, S, X, Y, Z = NMI()
    Q = NI()
    STUV = EI(Q)
    A = [0] * N
    A[0] = S
    BIT = 100000
    MASK = (1<<BIT)-1
    Ps = [0] * (N // BIT + 2)
    if S % 2:
        Ps[0] = 1
    for i in range(N-1):
        A[i+1] = (A[i] * X + Y) % Z
        if A[i+1] % 2:
            d, r = divmod(i+1, BIT)
            Ps[d] |= 1 << r

    for s, t, u, v in STUV:
        s -= 1
        u -= 1
        bl = (u + BIT-1) // BIT
        br = t // BIT
        idx = 0
        BIR = []
        PB = []
        while u < v:
            # print(u)
            if u < bl * BIT or u >= br * BIT:
                bi, r = divmod(u, BIT)
                st = s + idx
                sti, st_r = divmod(st, BIT)
                if (Ps[sti] >> st_r) & 1:
                    BIR.append([bi, r])

                # print(u+1, st+1)
                u += 1
                idx += 1
            else:
                bi, r = divmod(u, BIT)
                st = s + idx
                sti, st_r = divmod(st, BIT)
                if st_r == 0:
                    PB.append([bi, Ps[sti]])
                else:
                    tmp = Ps[sti] >> st_r
                    tmp |= Ps[sti+1] << (BIT-st_r)
                    tmp &= MASK
                    PB.append([bi, tmp])

                u += BIT
                idx += BIT

        for bi, r in BIR:
            Ps[bi] ^= 1 << r
        for bi, t in PB:
            Ps[bi] ^= t

    ans = []
    for i in range(N):
        b = (Ps[i//BIT] >> (i%BIT)) & 1
        if b:
            ans.append("O")
        else:
            ans.append("E")
    print("".join(ans))


if __name__ == "__main__":
    main()
