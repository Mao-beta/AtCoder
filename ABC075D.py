import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def compress(S):
    """ 座標圧縮 """

    S = set(S)
    zipped, unzipped = {}, {}
    for i, a in enumerate(sorted(S)):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped


def cum_2D(_A):
    """
    2次元リストAの累積和
    """
    from copy import deepcopy

    A = deepcopy(_A)
    H = len(A)
    W = len(A[0])
    for h in range(H):
        for w in range(W-1):
            A[h][w+1] += A[h][w]
    for w in range(W):
        for h in range(H-1):
            A[h+1][w] += A[h][w]

    return A


def area_sum(cum, hl, hr, wl, wr):
    """
    2次元累積和の行列cum（左と上は0）から、元の行列の[hl:hr, wl:wr]の範囲で和をとる
    """
    return cum[hr][wr] - cum[hl][wr] - cum[hr][wl] + cum[hl][wl]


def main():
    N, K = NMI()
    XY = [NLI() for _ in range(N)]
    X = [x for x, y in XY]
    Y = [y for x, y in XY]
    zX, uzX = compress(X)
    zY, uzY = compress(Y)
    grid = [[0]*(N+1) for _ in range(N+1)]
    for x, y in XY:
        zx, zy = zX[x], zY[y]
        grid[zx+1][zy+1] += 1

    cum = cum_2D(grid)

    ans = 1<<62
    for hl in range(N):
        for hr in range(hl+1, N+1):
            for wl in range(N):
                for wr in range(wl+1, N+1):
                    area = area_sum(cum, hl, hr, wl, wr)
                    if area >= K:
                        HL, HR = uzX[hl], uzX[hr-1]
                        WL, WR = uzY[wl], uzY[wr-1]
                        ans = min(ans, (HR-HL)*(WR-WL))

    print(ans)


if __name__ == "__main__":
    main()
