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


def cum_2D(A):
    """
    2次元リストAの累積和（左と上は0になる）
    """
    H = len(A)
    W = len(A[0])
    C = [[0]*(W+1) for _ in range(H+1)]

    for h in range(H):
        cw = 0
        for w in range(W):
            cw += A[h][w]
            if h == 0 and w == 0:
                C[h+1][w+1] = A[h][w]
            elif h == 0:
                C[h+1][w+1] = A[h][w] + C[h+1][w]
            elif w == 0:
                C[h+1][w+1] = A[h][w] + C[h][w+1]
            else:
                C[h+1][w+1] = C[h][w+1] + cw

    return C


def area_sum(cum, hl, hr, wl, wr):
    """
    2次元累積和の行列cum（左と上は0）から、元の行列の[hl:hr, wl:wr]の範囲で和をとる
    """
    return cum[hr][wr] - cum[hl][wr] - cum[hr][wl] + cum[hl][wl]


from collections import deque
def sliding_min(L, K):
    """
    Lの長さKの連続部分列それぞれの最小値のリストを返す
    """
    assert 1 <= K <= len(L)
    res = []
    D = deque()
    for i, x in enumerate(L):
        while D and L[D[-1]] >= x:
            D.pop()
        D.append(i) # L[i]がDの中で最大
        while D and D[0] <= i-K:
            D.popleft()
        res.append(L[D[0]])
    return res[K-1:]


def area_min_sliding(A, hl, wl):
    """
    グリッド内の大きさ固定の各矩形の最小値を全体でO(HW)
    最大値にしたいときは全部正負反転させてから使う
    res[i][j] = min(A[i:i+hl, j:j+wl])

    スライド最小値を取って転置してまた取って転置し直すとできる
    """
    res = []
    for h, row in enumerate(A):
        r = sliding_min(row, wl)
        res.append(r)

    res = [list(x) for x in zip(*res)]
    for w, row in enumerate(res):
        r = sliding_min(row, hl)
        res[w] = r

    res = [x for x in zip(*res)]
    return res


def main():
    H, W, h1, w1, h2, w2 = NMI()
    A = EI(H)
    C = cum_2D(A)
    # 白スタンプは黒スタンプに収まるとしてもよい
    h2 = min(h2, h1)
    w2 = min(w2, w1)

    # Black[h][w]: (h, w)を左上としたときの矩形和
    Black = [[0]*(W-w1+1) for _ in range(H-h1+1)]
    White = [[0] * (W - w2 + 1) for _ in range(H - h2 + 1)]
    
    for h in range(H-h1+1):
        for w in range(W-w1+1):
            Black[h][w] = area_sum(C, h, h+h1, w, w+w1)

    for h in range(H-h2+1):
        for w in range(W-w2+1):
            White[h][w] = area_sum(C, h, h+h2, w, w+w2)

    # 黒を固定したとき、白スタンプは(h1-h2+1)x(w1-w2+1)の領域を動く
    # (h,w)を左上とする (h1-h2+1)x(w1-w2+1)の領域のMaxを前計算
    # スライド最小値を使うので、正負反転してから戻す
    White_minus = [[-xx for xx in x] for x in White]
    White_max = area_min_sliding(White_minus, h1-h2+1, w1-w2+1)
    White_max = [[-xx for xx in x] for x in White_max]

    # (h,w)を左上とする黒スタンプ内で白スタンプを動かしたときの最大値を引く
    ans = 0
    for h in range(H-h1+1):
        for w in range(W-w1+1):
            ans = max(ans, Black[h][w] - White_max[h][w])
    print(ans)


if __name__ == "__main__":
    main()
