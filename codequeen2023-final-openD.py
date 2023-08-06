import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

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
    R, C, rs, cs, rt, ct = NMI()
    rs, cs, rt, ct = rs-1, cs-1, rt-1, ct-1
    M = 200005
    HM = 100000
    # M = 8
    # HM = 4
    DS = [[0] * M for _ in range(4)]
    DT = [[0] * M for _ in range(4)]

    def search(qr, qc):
        res = []
        DR = [0, 0, 1, -1, 1, -1, 1, -1]
        DC = [1, -1, 0, 0, 1, 1, -1, -1]
        for dr, dc in zip(DR, DC):
            r, c = qr, qc
            while 0 <= r+dr < R and 0 <= c+dc < C:
                r += dr
                c += dc
                res.append((r, c))
        return res

    RS = search(rs, cs)
    RT = search(rt, ct)

    for r, c in RS:
        DS[0][r] += 1
        DS[1][c] += 1
        DS[2][r+c] += 1
        DS[3][r-c+HM] += 1

    for r, c in RT:
        DT[0][r] += 1
        DT[1][c] += 1
        DT[2][r+c] += 1
        DT[3][r-c+HM] += 1

    ans = 0
    for SS, TT in zip(DS, DT):
        for s, t in zip(SS, TT):
            ans += s * t

    same = set(RS) & set(RT)
    ans -= len(same) * 4
    print(ans)


if __name__ == "__main__":
    main()
