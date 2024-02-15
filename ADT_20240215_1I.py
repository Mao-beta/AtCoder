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


def main():
    N = NI()
    B = 1<<N
    C = EI(B)

    INF = 10**18
    # 上からi段目でjが勝ち上がってるときのそれ以下のMax
    dp_win = [[-INF]*B for _ in range(N+1)]
    # 試合i以下で勝ち上がりがないときのMax
    dp_lose = [-INF] * (2*B)

    # 試合gameを終えたときの全体のMax
    # 決勝が試合0(h=0, w=0)、左が2i+1(h+1, 2w), 右が2i+2(h+1, 2w+1)
    def rec(i, h, w, num):
        if h >= N:
            # 人pのみのノード、N段目
            p = i
            dp_win[N][p-(B-1)] = 0
            dp_lose[p] = 0
            return

        rec(2*i+1, h+1, 2*w, num//2)
        rec(2*i+2, h+1, 2*w+1, num//2)

        # 帰りがけ
        half = num*w + num//2
        for p in range(num*w, num*(w+1)):
            # print(i, h, w, p)
            if p < half:
                dp_win[h][p] = max(dp_win[h][p], dp_win[h+1][p] + dp_lose[2*i+2])
                dp_lose[i] = max(dp_lose[i], dp_win[h+1][p] + dp_lose[2*i+2] + C[p][N-1-h])
            else:
                dp_win[h][p] = max(dp_win[h][p], dp_win[h+1][p] + dp_lose[2*i+1])
                dp_lose[i] = max(dp_lose[i], dp_win[h+1][p] + dp_lose[2*i+1] + C[p][N-1-h])

    rec(0, 0, 0, B)
    print(dp_lose[0])


if __name__ == "__main__":
    main()
