import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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
    N = SI()
    L = len(N)
    M = 150
    # i個決めて、現在の桁和がnow、jで割った余りがk, 最外側に未満確定かどうか
    dp = [[[[[0]*M for _ in range(M+1)] for _ in range(M+1)] for _ in range(L+1)] for _ in range(2)]
    for j in range(1, M+1):
        dp[0][0][0][j][0] = 1

    for i in range(L):
        n = int(N[0])
        ni = i+1
        for now in range(M+1):
            for j in range(1, M+1):
                for k in range(j):
                    for same in range(2):
                        if same:
                            xlim = n
                        else:
                            xlim = 9
                        if dp[same][i][now][j][k] == 0:
                            continue

                        for x in range(xlim+1):
                            if same and x == xlim:
                                nsame = 1
                            else:
                                nsame = 0
                            nj = j
                            nk = (k + x) % j
                            nnow = now + x
                            print(ni, nnow, nj, nk, i, now, j, k)
                            dp[nsame][ni][nnow][nj][nk] += dp[same][i][now][j][k]

    ans = 0
    for j in range(1, M+1):
        for same in range(2):
            ans += dp[same][L][j][j][0]
    print(ans)


if __name__ == "__main__":
    main()
