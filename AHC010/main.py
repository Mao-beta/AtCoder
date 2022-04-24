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


# LURD
to = [
    [1, 0, -1, -1], # LU
    [3, -1, -1, 0], # L  D
    [-1, -1, 3, 2], #   RD
    [-1, 2, 1, -1], #  UR
    [1, 0, 3, 2],   # 」「
    [3, 2, 1, 0],   #
    [2, -1, 0, -1], # ー
    [-1, 3, -1, 1], # |
]

# iからjにするときの回転回数
rot = [[0, 1, 2, 3, -1, -1, -1, -1],
       [3, 0, 1, 2, -1, -1, -1, -1],
       [2, 3, 0, 1, -1, -1, -1, -1],
       [1, 2, 3, 0, -1, -1, -1, -1],
       [-1, -1, -1, -1, 0, 1, -1, -1],
       [-1, -1, -1, -1, 1, 0, -1, -1],
       [-1, -1, -1, -1, -1, -1, 0, 1],
       [-1, -1, -1, -1, -1, -1, 1, 0]]



def main():
    N = 30
    G = [[int(s) for s in SI()] for _ in range(N)]
    ans = [[0] * N for _ in range(N)]

    fix = [[0]*N for _ in range(N)]
    # 左上から丸を作っていく 24 15 35 04
    for i in range(N-1):
        for j in range(N-1):
            ok = True
            tmp = [0, 0, 0, 0]
            for k in range(4):
                ni = i + k // 2
                nj = j + k % 2
                if G[ni][nj] >= 6:
                    ok = False
                    break

                if fix[ni][nj] and G[ni][nj] < 4:
                    # print(i, j)
                    ok = False
                    break

                if fix[ni][nj] and k == 0 and G[ni][nj] != 4:
                    ok = False
                    break

                if fix[ni][nj] and k == 1 and G[ni][nj] != 5:
                    ok = False
                    break

                g = G[ni][nj]
                goto = [2, 1, 3, 0]
                goto2 = [4, 5, 5, 4]
                if g < 4:
                    tmp[k] = goto[k]
                else:
                    tmp[k] = goto2[k]

            if ok:
                # print(i, j)

                for k in range(4):
                    ni = i + k // 2
                    nj = j + k % 2
                    fix[ni][nj] = 1
                    ans[ni][nj] += rot[G[ni][nj]][tmp[k]]
                    ans[ni][nj] %= 4
                    G[ni][nj] = tmp[k]

    # 斜めに隣接する丸をつなぐ
    for i in range(1, N-1):
        for j in range(1, N-1):
            if G[i][j] == 4:
                ok = True
                for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [1, 1]]:
                    if fix[i+di][j+dj] == 0:
                        ok = False
                if ok:
                    ans[i][j] += 1
                    ans[i][j] %= 4

            elif G[i][j] == 5:
                ok = True
                for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, -1], [-1, 1]]:
                    if fix[i+di][j+dj] == 0:
                        ok = False
                if ok:
                    ans[i][j] += 1
                    ans[i][j] %= 4

    for row in ans:
        print("".join(map(str, row)), end="")
    print()


if __name__ == "__main__":
    main()
