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
    xa, ya, xb, yb, xc, yc = NMI()
    xb -= xa
    yb -= ya
    xc -= xa
    yc -= ya
    DX = [0, 0, 1, -1]
    DY = [1, -1, 0, 0]

    def dist(P, Q):
        return abs(P[0]-Q[0]) + abs(P[1]-Q[1])

    def is_right(A, B, C):
        # 荷物B、ゴールCに対してAの位置は適切か？
        # ただしAとBは隣接
        return (A[0]-B[0]) * (C[0]-B[0]) < 0 or (A[1]-B[1]) * (C[1]-B[1]) < 0

    def carry(A, B, C):
        # BをCに運ぶ回数
        # 荷物B、ゴールCに対してAの位置は適切とする
        if A[0] == B[0] == C[0] or A[1] == B[1] == C[1]:
            return dist(B, C)
        else:
            return dist(B, C) + 2

    def move(A, B):
        # 荷物Bの周囲4マスへのAからの移動回数
        res = []
        for dx, dy in zip(DX, DY):
            tx, ty = B[0]+dx, B[1]+dy
            if A[1] == B[1] == ty and (A[0]-B[0]) * (tx-B[0]) < 0:
                res.append([tx, ty, dist(A, [tx, ty]) + 2])
            elif A[0] == B[0] == tx and (A[1]-B[1]) * (ty-B[1]) < 0:
                res.append([tx, ty, dist(A, [tx, ty]) + 2])
            else:
                res.append([tx, ty, dist(A, [tx, ty])])
        return res

    Ps = move((0, 0), (xb, yb))
    ans = 10**18
    for x, y, m in Ps:
        if not is_right((x, y), (xb, yb), (xc, yc)):
            continue
        ans = min(ans, m + carry((x, y), (xb, yb), (xc, yc)))

    print(ans)


if __name__ == "__main__":
    main()
