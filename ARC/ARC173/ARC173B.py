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


def online(P, Q, R):
    PQ = [Q[0]-P[0], Q[1]-P[1]]
    PR = [R[0]-P[0], R[1]-P[1]]
    return PQ[0] * PR[1] == PQ[1] * PR[0]

def main():
    N = NI()
    XY = EI(N)
    B = [0] * N
    Z = [[set() for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if online(XY[i], XY[j], XY[k]):
                    B[i] += 1
                    B[j] += 1
                    B[k] += 1
                    Z[i][j].add(k)
                    Z[j][k].add(i)
                    Z[k][i].add(j)
                    Z[i][k].add(j)
                    Z[k][j].add(i)
                    Z[j][i].add(k)

    BI = [[b, i] for i, b in enumerate(B)]
    BI.sort()
    ans = 0
    while len(BI) >= 3:
        pi = BI[-1][1]
        ok = False
        for q in range(len(BI)-2, 0, -1):
            qi = BI[q][1]
            for r in range(q-1, -1, -1):
                ri = BI[r][1]
                if ri not in Z[pi][qi]:
                    ans += 1
                    # print(pi, qi, ri)
                    BI.pop()
                    BI.pop(q)
                    BI.pop(r)
                    ok = True
                if ok:
                    break
            if ok:
                break
        if not ok:
            BI.pop()

    print(ans)


if __name__ == "__main__":
    main()
