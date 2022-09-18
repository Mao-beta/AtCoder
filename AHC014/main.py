import sys
import math
import bisect
import time
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations
import pprint

try:
    import numpy
    IS_LOCAL = True
except:
    IS_LOCAL = False


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


# URDL UR RD DL UL
DX = [0, 1, 0, -1]
DX2 = [1, 1, -1, -1]
DY = [1, 0, -1, 0]
DY2 = [1, -1, 1, -1]


def on_board(h, w, N):
    return 0 <= h < N and 0 <= w < N


def output(ans):
    print(len(ans))
    for row in ans:
        print(*row)


def output_file(ans, outpath):
    with open(outpath, "w") as f:
        f.write(str(len(ans)) + "\n")
        for row in ans:
            f.write(" ".join(map(str, row)) + "\n")


def direction_search(now_x, now_y, dx, dy, N, G):
    # ある点から特定の方向に探索し、当たった点の座標を返す
    # なければ(-1, -1)
    x = -1
    y = -1
    while on_board(now_x + dx, now_y + dy, N):
        now_x += dx
        now_y += dy
        if G[now_x][now_y]:
            x = now_x
            y = now_y
            break

    return x, y


def search(x1, y1, N, G):
    # 8方向×回転方向2つのの16回探索して、座標とスコアを返す
    res = []

    for di in range(4):
        dx, dy = DX[di], DY[di]
        di2 = (di+1) % 4
        dx2, dy2 = DX[di2], DY[di2]

        x2, y2 = direction_search(x1, y1, dx, dy, N, G)
        x4, y4 = direction_search(x1, y1, dx2, dy2, N, G)

        if x2 == -1 or x4 == -1:
            continue

        x3, y3 = direction_search(x2, y2, dx2, dy2, N, G)
        x3_, y3_ = direction_search(x4, y4, dx, dy, N, G)

        if x3 == -1 or x3_ == -1:
            continue

        if x3 == x3_ and y3 == y3_:
            res.append([x1, y1, x2, y2, x3, y3, x4, y4])


    for di in range(4):
        dx, dy = DX2[di], DY2[di]
        di2 = (di+1) % 4
        dx2, dy2 = DX2[di2], DY2[di2]

        x2, y2 = direction_search(x1, y1, dx, dy, N, G)
        x4, y4 = direction_search(x1, y1, dx2, dy2, N, G)

        if x2 == -1 or x4 == -1:
            continue

        x3, y3 = direction_search(x2, y2, dx2, dy2, N, G)
        x3_, y3_ = direction_search(x4, y4, dx, dy, N, G)

        if x3 == -1 or x3_ == -1:
            continue

        if x3 == x3_ and y3 == y3_:
            res.append([x1, y1, x2, y2, x3, y3, x4, y4])

    return res



def sign(x):
    if x == 0:
        return 0
    return x // abs(x)


def rect_edges(rect):
    P = rect[:] + [rect[0], rect[1]]
    res = set()
    for i in range(4):
        x1, y1 = P[i*2], P[i*2+1]
        x2, y2 = P[i*2+2], P[i*2+3]
        dx = sign(x2-x1)
        dy = sign(y2-y1)
        while x1 != x2 or y1 != y2:
            e = [x1, y1, x1+dx, y1+dy]
            if e[0] > e[2]:
                e[0], e[2] = e[2], e[0]
                e[1], e[3] = e[3], e[1]
            elif e[0] == e[2] and e[1] > e[3]:
                e[1], e[3] = e[3], e[1]
            res.add(tuple(e))
            x1 += dx
            y1 += dy

    return res


def main(N, M, XY):
    START_TIME = time.time()

    ans = []

    E = set()

    ORDER = []
    m = (N-1) // 2
    for x in range(N):
        for y in range(N):
            ORDER.append([x, y, (x-m)**2 + (y-m)**2 + 1])
    ORDER.sort(key=lambda x: -x[2])

    G = [[0]*N for _ in range(N)]
    for x, y in XY:
        G[x][y] = 1


    ratio = 0.8
    gap = 0.01

    while True:
        K = int(N**2 * ratio)
        K = min(N**2, K)

        for x, y, s in ORDER[:K]:
            if G[x][y]:
                continue

            res = search(x, y, N, G)

            if res:
                for rect in res:
                    edges = rect_edges(rect)

                    if len(E & edges) == 0:
                        # print(rect)
                        # print(edges)
                        # print(E)
                        G[x][y] = 1
                        E |= edges
                        ans.append(rect)
                        break

        if time.time() - START_TIME > 2.7:
            break

        ratio += gap

    # print(N, M, int((ratio - 0.8) / gap))
    return ans, G


def take_input(path=None):
    if path:
        with open(path, mode="r") as f:
            inputs = f.readlines()
            N, M = map(int, inputs[0].split())
            XY = []
            for i in range(M):
                xy = list(map(int, inputs[1+i].split()))
                XY.append(xy)

    else:
        N, M = NMI()
        XY = [NLI() for _ in range(M)]

    return N, M, XY


# IS_LOCAL = False

def calc_local(N, M, XY, ans, G):
    w = 0
    m = (N-1) // 2
    s = 0
    for x in range(N):
        for y in range(N):
            k = (x-m) ** 2 + (y-m) ** 2 + 1
            if G[x][y]:
                w += k
            s += k
    score = round(10**6 * N**2 * w / M / s)
    return score


if __name__ == "__main__":
    if IS_LOCAL:
        import pandas as pd
        df = []

        for i in range(100):
            path = f"./in/{str(i).zfill(4)}.txt"
            inputs = take_input(path)
            ans, G = main(*inputs)
            outpath = f"./out/{str(i).zfill(4)}.txt"
            output_file(ans, outpath)
            score = calc_local(*inputs, ans, G)
            df.append([f"{str(i).zfill(4)}.txt", inputs[0], inputs[1], score])

        df = pd.DataFrame(df, columns=["name", "N", "M", "score"])
        df.to_csv("./scores.csv", index=False)

    else:
        ans = main(*take_input())
        output(ans)

