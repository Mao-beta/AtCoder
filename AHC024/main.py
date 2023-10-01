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
    N, M = NMI()
    C = EI(N)
    G = [set() for _ in range(M+1)]

    DH = [0, 0, 1, -1]
    DW = [1, -1, 0, 0]

    DH8 = [0, 0, 1, -1, 1, 1, -1, -1]
    DW8 = [1, -1, 0, 0, 1, -1, 1, -1]

    cnts = [0] * (M+1)

    def in_grid(h, w):
        return 0 <= h < N and 0 <= w < N

    for h in range(N):
        for w in range(N):
            c1 = C[h][w]
            if h < N-1:
                c2 = C[h+1][w]
                G[c1].add(c2)
                G[c2].add(c1)
            if w < N-1:
                c3 = C[h][w+1]
                G[c1].add(c3)
                G[c3].add(c1)
            if h in [0, N-1] or w in [0, N-1]:
                G[0].add(c1)
                G[c1].add(0)

            cnts[c1] += 1


    def clean(h, w):
        # 1マスしかなかったら放置
        if cnts[C[h][w]] <= 1:
            return

        # 8方向に4色あったらそっとしておく
        Cs = []
        for dh, dw in zip(DH8, DW8):
            nh, nw = h + dh, w + dw
            if not in_grid(nh, nw):
                Cs.append(0)
            else:
                Cs.append(C[nh][nw])

        if len(set(Cs)) >= 4:
            return

        # 三方を囲まれていたらその色にする
        Cs = []
        for dh, dw in zip(DH, DW):
            nh, nw = h+dh, w+dw
            if not in_grid(nh, nw):
                Cs.append(0)
            else:
                Cs.append(C[nh][nw])

        S_cs = set(Cs)
        if len(S_cs) == 2 and 0 not in S_cs and Cs.count(C[h][w]) == 1:
            S_cs.discard(C[h][w])
            x = S_cs.pop()
            cnts[C[h][w]] -= 1
            C[h][w] = x
            cnts[x] += 1

        # # 自分, x, x, yに囲まれているとき、xとyがもともと隣接ならxにする
        # # ### 最後の隣接マスを消してしまう
        # S_cs = set(Cs)
        # if len(S_cs) == 3 and 0 not in S_cs and Cs.count(C[h][w]) == 1:
        #     S_cs.discard(C[h][w])
        #     for x in list(S_cs):
        #         if Cs.count(x) == 2:
        #             S_cs.discard(x)
        #             y = S_cs.pop()
        #             if y in G[x]:
        #                 cnts[C[h][w]] -= 1
        #                 C[h][w] = x
        #                 cnts[x] += 1
        #             break

        S_cs = set(Cs)
        if Cs.count(0) == 1 and len(S_cs) == 3 and Cs.count(C[h][w]) == 1:
            for x in S_cs:
                if Cs.count(x) == 2:
                    cnts[C[h][w]] -= 1
                    C[h][w] = x
                    cnts[x] += 1
                    break

    for _ in range(3):
        for h in range(N):
            for w in range(N):
                clean(h, w)

        for row in C:
            print(*row)

        for h in range(N-1, -1, -1):
            for w in range(N-1, -1, -1):
                clean(h, w)

        for row in C:
            print(*row)

    # 外側から白にできるだけしていく
    # 白にした結果もその色が連結で、隣接も変わらなければOK



if __name__ == "__main__":
    main()
