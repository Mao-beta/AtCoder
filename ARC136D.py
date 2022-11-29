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
    A = NLI()
    # ex. D[3][5][9][4][1][2] 各桁が359412の各桁以下であるaの数
    D = [[[[[[0]*11 for _ in range(11)] for _ in range(11)] for _ in range(11)] for _ in range(11)] for _ in range(11)]

    for a in A:
        i, j, k, l, m, n = map(int, str(a).zfill(6))
        D[i][j][k][l][m][n] += 1

    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    for m in range(10):
                        for n in range(10):
                            D[i][j][k][l][m][n+1] += D[i][j][k][l][m][n]

    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    for n in range(10):
                        for m in range(10):
                            D[i][j][k][l][m+1][n] += D[i][j][k][l][m][n]

    for i in range(10):
        for j in range(10):
            for k in range(10):
                for n in range(10):
                    for m in range(10):
                        for l in range(10):
                            D[i][j][k][l+1][m][n] += D[i][j][k][l][m][n]

    for i in range(10):
        for j in range(10):
            for n in range(10):
                for l in range(10):
                    for m in range(10):
                        for k in range(10):
                            D[i][j][k+1][l][m][n] += D[i][j][k][l][m][n]

    for i in range(10):
        for n in range(10):
            for k in range(10):
                for l in range(10):
                    for m in range(10):
                        for j in range(10):
                            D[i][j+1][k][l][m][n] += D[i][j][k][l][m][n]

    for n in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    for m in range(10):
                        for i in range(10):
                            D[i+1][j][k][l][m][n] += D[i][j][k][l][m][n]

    ans = 0
    for a in A:
        i, j, k, l, m, n = map(int, str(a).zfill(6))
        # print(a, D[9-i][9-j][9-k][9-l][9-m][9-n])
        ans += D[9-i][9-j][9-k][9-l][9-m][9-n]
        if max(i, j, k, l, m, n) <= 4:
            ans -= 1

    print(ans//2)


if __name__ == "__main__":
    main()
