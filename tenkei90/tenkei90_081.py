import sys
import math
from collections import defaultdict

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def _cum_2D(A):
    """
    2次元リストAの累積和
    """
    H = len(A)
    W = len(A[0])
    C = [[0]*W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            C[h][w] = A[h][w]

    for h in range(H):
        for w in range(W-1):
            C[h][w+1] += C[h][w]
    for w in range(W):
        for h in range(H-1):
            C[h+1][w] += C[h][w]

    return C


def cum_2D(A):
    """
    2次元リストAの累積和
    """
    H = len(A)
    W = len(A[0])
    C = [[0]*W for _ in range(H)]

    for h in range(H):
        cw = 0
        for w in range(W):
            if h == 0 and w == 0:
                C[h][w] = A[h][w]
            elif h == 0:
                C[h][w] = A[h][w] + C[h][w-1]
            elif w == 0:
                C[h][w] = A[h][w] + C[h-1][w]
            else:
                cw += A[h][w]
                C[h][w] = C[h-1][w] + cw

    return C


def area_sum(cum, hl, hr, wl, wr):
    """
    2次元累積和の行列cum（左と上は0）から、元の行列の[hl:hr, wl:wr]の範囲で和をとる
    """
    return cum[hr][wr] - cum[hl][wr] - cum[hr][wl] + cum[hl][wl]


def main():
    N, K = NMI()
    AB = [NLI() for _ in range(N)]
    M = 5001
    grid = [[0]*M for _ in range(M)]
    for a, b in AB:
        grid[a][b] += 1

    cum = cum_2D(grid)

    ans = 0
    for al in range(M):
        for bl in range(M):
            ar = al + K + 1
            br = bl + K + 1
            try:
                ans = max(ans, area_sum(cum, al, ar, bl, br))
            except:
                break

    print(ans)


if __name__ == "__main__":
    main()
