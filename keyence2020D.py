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
    B = NLI()

    INF = 10**10
    M = 50
    # dp[U][x]: すでに置いたカードの集合がUで、
    # 列の最後の値がxのときの転倒数の最小値
    dp = [[INF]*(M+1) for _ in range(1<<N)]
    dp[0][0] = 0

    for U in range(1<<N):
        un = bin(U).count("1") # Uに立っている1の数（左に何枚置いたか）

        for i in range(N):
            if (U >> i) & 1: # 右からi番目(0-index)のbitが1か？
                continue
            goto = U | (1<<i) # Uにi番目のカードをつけ足した後の状態

            # 置きたい位置と元の位置の差が奇数ならB、偶数ならA
            y = B[i] if (un - i) % 2 else A[i]

            # Uにi番目より後のカードが含まれていたら転倒数+1
            rev = 0
            for j in range(i+1, N):
                if (U >> j) & 1:
                    rev += 1

            # dp遷移 yが遷移元のx以上なら置ける
            for x in range(M+1):
                if x > y:
                    continue
                if dp[U][x] == INF:
                    continue

                # print(bin(U)[2:].zfill(N), bin(goto)[2:].zfill(N), x, y, rev)
                dp[goto][y] = min(dp[goto][y], dp[U][x] + rev)

    # print(*dp, sep="\n")
    ans = min(dp[-1])
    print(ans if ans < INF else -1)


if __name__ == "__main__":
    main()
