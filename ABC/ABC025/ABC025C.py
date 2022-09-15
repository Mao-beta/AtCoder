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


def main():
    B = [NLI() for _ in range(2)]
    C = [NLI() for _ in range(3)]

    G = [[0]*3 for _ in range(3)]


    def calc():
        a, b = 0, 0
        for h in range(2):
            for w in range(3):
                if G[h][w] * G[h+1][w] > 0:
                    a += B[h][w]
                else:
                    b += B[h][w]

        for h in range(3):
            for w in range(2):
                if G[h][w] * G[h][w+1] > 0:
                    a += C[h][w]
                else:
                    b += C[h][w]
        return a, b


    def rec(turn, player):
        """
        :param turn: turn==9なら終了して得点計算
        :param player: 1なら直大、-1なら直子
        :return: score
        """
        # print(turn)
        # print(*G, sep="\n")

        if turn >= 9:
            a, b = calc()
            return a, b

        res = []

        for h in range(3):
            for w in range(3):
                if G[h][w] != 0:
                    continue

                G[h][w] = player
                a, b = rec(turn+1, player*(-1))
                res.append([a, b])
                G[h][w] = 0

        if player > 0:
            res.sort(key=lambda x: x[0])
            return res[-1]
        else:
            res.sort(key=lambda x: x[1])
            return res[-1]

    a, b = rec(0, 1)
    print(a)
    print(b)


if __name__ == "__main__":
    main()
