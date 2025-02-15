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
    if N == 1:
        print(1)
        return

    # 0～N-1の順列のうち、隣接2項の差が2にならないものを数え上げる
    # 順列は挿入DP
    # i未満まであって、iを新たに入れる遷移を考える
    # アウトな箇所の個数を管理する
    # (i-4, i-2)の間に入れると±0、それ以外に入れると-1
    # 遷移先の↑を求めるために(i-3, i-1)間もあるか持っておく必要がある
    # dp[i][j][f][g]: i個見て、アウトがj個(<i)ある fは(i-4, i-2)、gは(i-3, i-1)の存在
    dp = [[[[0]*2 for _ in range(2)] for _ in range(N)] for _ in range(N+1)]
    dp[2][0][0][0] = 2
    for i in range(2, N):
        # iを入れる
        for j in range(N):
            for f in range(2):
                for g in range(2):
                    dp[i][j][f][g] %= MOD
                    d = dp[i][j][f][g]
                    if d == 0:
                        continue

                    # (i-4, i-2)に入れる
                    if f:
                        dp[i+1][j][g][1] += d
                    # i-2の横に入れる(f=1のときは上でやってる)
                    dp[i+1][j+1][g][1] += d * (2-f)

                    # (i-3, i-1)に入れる
                    if g:
                        dp[i+1][j-1][0][0] += d
                    # それ以外のアウトを減らす(j個のうち、(i-4, i-2)と(i-3, i-1)は解決済み)
                    dp[i+1][j-1][g][0] += d * (j-f-g)
                    # 残りに入れる(i+1個のうち、j+2(j個とi-2の横2個)以外だが、f=1のときは重複)
                    dp[i+1][j][g][0] += d * (i+1-(j+2-f))

    print(dp[N][0][0][0] % MOD)


if __name__ == "__main__":
    main()
