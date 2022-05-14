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


def area8(P, Q, R):
    # 三角形の面積の8倍
    x1, y1 = P
    x2, y2 = Q
    x3, y3 = R
    a, b, c, d = x2-x1, y2-y1, x3-x1, y3-y1

    return abs(a * d - b * c) * 4


def main():
    N = NI()
    XY = [NLI() for _ in range(N)]

    # 常に面積の8倍を考える
    # 総面積Sを前計算
    S = 0
    for i in range(N-2):
        S += area8(XY[0], XY[i+1], XY[i+2])

    # 問題文中の"a"の8倍
    target = S // 4
    # "b"の8倍
    now = 0

    p1 = 0
    p2 = 1

    INF = 10**20
    ans = INF

    # 尺取り法
    for p0 in range(N):
        # S//4未満なら前に足す
        while now < target:
            p1 += 1
            p2 += 1
            now += area8(XY[p0], XY[p1%N], XY[p2%N])
            ans = min(ans, abs(now - target))

        # 超えていたら後ろから引く
        now -= area8(XY[p0], XY[(p0+1)%N], XY[p2%N])
        ans = min(ans, abs(now - target))

    print(ans)


if __name__ == "__main__":
    main()
