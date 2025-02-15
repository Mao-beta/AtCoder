import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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
    L = EI(N)
    ans = 0

    def cross(A, B):
        return A[0]*B[1] - A[1]*B[0]

    def check(P, Q, R, S):
        if P == Q:
            return 0
        # 直線PQは点Rと点Sの間を通るか？
        PQ = [Q[0]-P[0], Q[1]-P[1]]
        PR = [R[0]-P[0], R[1]-P[1]]
        PS = [S[0]-P[0], S[1]-P[1]]
        pqxpr = cross(PQ, PR)
        pqxps = cross(PQ, PS)
        return pqxpr * pqxps <= 0

    Ps = []
    for a, b, c, d in L:
        Ps.append([a, b])
        Ps.append([c, d])

    for px, py in Ps:
        for qx, qy in Ps:
            tmp = 0
            for ri, (ar, br, cr, dr) in enumerate(L):
                tmp += check([px, py], [qx, qy], [ar, br], [cr, dr])
            ans = max(ans, tmp)

    print(ans)


if __name__ == "__main__":
    main()
