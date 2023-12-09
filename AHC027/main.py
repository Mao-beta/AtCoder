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


"""
めも：
DFS探索を最適化していく？
あるマスからどちらに進むかをプレイアウトで決めていく
40x40の際の計算量が足りるか？足りそうではある

重いマスは何回も通りたいような気がする
ハブみたいにしてそこから小さい部分木をたくさん生やしたいかも
重い領域の中心はどう定めるか？

重いエリアは定期的に様子見しつつ、行ってないマスを埋めてくのが直感的にはよさそう

サンプルコードは帰り道もうねうねしていて、軽いマスでそれをやるのは無駄そう
軽かったらスルーで重かったらちゃんと帰りも通るのがいいが…そんなんできるか？
"""


def main():
    N = NI()
    h = [list(map(int, SI())) for _ in range(N - 1)]
    v = [list(map(int, SI())) for _ in range(N)]
    d = [list(map(int, input().split())) for _ in range(N)]

    # タイミングを記録
    # visited = [[[] for _ in range(N)] for _ in range(N)]

    DIJ = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    DIR = "RDLU"

    def playout(V, S, i, j):
        """
        V, S, i, jから始めたときの
        :param V: 今までのvisited
        :param S: 今までのstack
        :param i, j: 始点
        """
        V = [row[:] for row in V]
        S = S.copy()

        start = (i, j)

        S = deque()
        S.append(start)

        while S:
            now_h, now_w = S.popleft()
            now_step = [now_h][now_w]

            for d, (dh, dw) in enumerate(DIJ):
                goto_h = now_h + dh
                goto_w = now_w + dw
                goto_step = now_step + 1

                if goto_h < 0 or goto_h >= N or goto_w < 0 or goto_w >= N:
                    continue
                if (dh == 0 and v[now_h][min(now_w, goto_w)]) or (dw == 0 and h[min(now_h, goto_h)][now_w]):
                    continue
                if 0 <= [goto_h][goto_w] <= goto_step:
                    continue

                S.append((goto_h, goto_w))
                [goto_h][goto_w] = goto_step

    import random
    def dfs_randomdir(i, j):
        visited[i][j] = True
        dir_order = list(range(4))
        random.shuffle(dir_order)
        for dir in dir_order:
            di, dj = DIJ[dir]
            i2 = i + di
            j2 = j + dj
            if 0 <= i2 < N and 0 <= j2 < N and not visited[i2][j2]:
                if di == 0 and v[i][min(j, j2)] == 0 or dj == 0 and h[min(i, i2)][j] == 0:
                    print(DIR[dir], end='')
                    dfs_randomdir(i2, j2)
                    print(DIR[(dir + 2) % 4], end='')

    def dfs(i, j):
        visited[i][j] = True
        dir_order = list(range(4))
        for dir in dir_order:
            di, dj = DIJ[dir]
            i2 = i + di
            j2 = j + dj
            if 0 <= i2 < N and 0 <= j2 < N and not visited[i2][j2]:
                if di == 0 and v[i][min(j, j2)] == 0 or dj == 0 and h[min(i, i2)][j] == 0:
                    print(DIR[dir], end='')
                    dfs(i2, j2)
                    print(DIR[(dir + 2) % 4], end='')

    visited = [[False for _ in range(N)] for _ in range(N)]
    dfs_randomdir(0, 0)
    print()
    visited = [[False for _ in range(N)] for _ in range(N)]
    dfs(0, 0)
    # dfs_randomdir(0, 0)
    print()


if __name__ == "__main__":
    main()
