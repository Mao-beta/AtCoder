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
    N = NI()
    S = [[1 if s == "#" else 0 for s in SI()] for _ in range(N)]
    # print(*S, sep="\n")

    for h in range(N):
        for w in range(N):
            yoko = 0
            tate = 0
            hisi = 0
            misi = 0

            for i in range(6):
                if 0 <= h < N and 0 <= w+i < N:
                    yoko += S[h][w+i]
                else:
                    yoko = 0
                if 0 <= h+i < N and 0 <= w < N:
                    tate += S[h+i][w]
                else:
                    tate = 0
                if 0 <= h+i < N and 0 <= w-i < N:
                    hisi += S[h+i][w-i]
                else:
                    hisi = 0
                if 0 <= h+i < N and 0 <= w+i < N:
                    misi += S[h+i][w+i]
                else:
                    misi = 0

            # print(h, w)
            # print(yoko, tate, hisi, misi)

            if max(yoko, tate, hisi, misi) >= 4:
                print("Yes")
                exit()

    print("No")


if __name__ == "__main__":
    main()
