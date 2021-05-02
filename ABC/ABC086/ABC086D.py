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


# 二次元累積和から[xa, xb), [ya, yb)の部分の合計を取得する
def get_num_in_area(xy_cum, xa, xb, ya, yb):
    X, Y = len(xy_cum), len(xy_cum[0])
    xa = min(X-1, max(0, xa))
    xb = min(X-1, max(0, xb))
    ya = min(Y-1, max(0, ya))
    yb = min(Y-1, max(0, yb))
    return xy_cum[xb][yb] - xy_cum[xa][yb] - xy_cum[xb][ya] + xy_cum[xa][ya]


def main():
    N, K = NMI()

    # 盤面をK*Kに制限し、そのマスに白黒がいくつあるか保持
    W = [[0] * K for _ in range(K)]
    B = [[0] * K for _ in range(K)]

    # xとyはmod 2Kしても色は変化しない
    # x, yがそれぞれKより大きいとき色を反転してKずらす
    for _ in range(N):
        x, y, c = SI().split()
        x = int(x) % (2*K)
        y = int(y) % (2*K)
        c = 1 if c == "B" else 0
        if x >= K:
            x -= K
            c = 1 - c
        if y >= K:
            y -= K
            c = 1 - c
        if c:
            B[x][y] += 1
        else:
            W[x][y] += 1

    # 二次元累積和初期化
    W_cum = [[0]*(K+1) for _ in range(K+1)]
    B_cum = [[0]*(K+1) for _ in range(K+1)]

    # それぞれの座標について1つ上、1つ左を足して左上を引いて現在地を足すと新しい累積和
    for x in range(K):
        for y in range(K):
            now_w = W[x][y]
            now_b = B[x][y]
            W_cum[x+1][y+1] = W_cum[x][y+1] + W_cum[x+1][y] - W_cum[x][y] + now_w
            B_cum[x+1][y+1] = B_cum[x][y+1] + B_cum[x+1][y] - B_cum[x][y] + now_b

    # get_num_in_areaで累積和の行列からスライスして計算していく
    # 色の境界を動かして全探索
    ans = 0
    for x_border in range(K):
        for y_border in range(K):
            num_w = 0
            num_b = 0
            # 交点から左上と右下の領域をみる
            D = [(0, 0), (-1, -1)]
            for dx, dy in D:
                xa = x_border + dx * K
                xb = xa + K
                ya = y_border + dy * K
                yb = ya + K
                num_w += get_num_in_area(W_cum, xa, xb, ya, yb)
                num_b += get_num_in_area(B_cum, xa, xb, ya, yb)
            # 交点の左上と右下が白のパターン（WB）、その反転（BW）の大きいほうを取る
            # WBでは見た領域が白なので、領域内の白の数＋（黒の全体数－領域内の黒の数）
            WB = num_w + B_cum[-1][-1] - num_b
            BW = N - WB
            ans = max(ans, WB, BW)

    print(ans)


if __name__ == "__main__":
    main()
