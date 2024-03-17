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
    Ns = NLI()
    g = 0
    for n in Ns:
        g ^= n % 4
    if g:
        print("Taro")
    else:
        print("Jiro")

def _main():
    Ns = NLI()
    S = sum(Ns)
    # dp[n0][n1][n2][n3][h0] h1=S-(n0+n1+n2+n3)
    # 上の状態で回されたら勝てるか
    dp = [[[[[0]*(S+1)
             for _ in range(Ns[3]+1)] for _ in range(Ns[2]+1)]
                for _ in range(Ns[1]+1)] for _ in range(Ns[0]+1)]
    for h0 in range(S+1):
        h1 = S - h0
        if h0 > h1:
            x = 1
        elif h0 < h1:
            x = -1
        else:
            x = 0
        dp[0][0][0][0][h0] = x

    for n0 in range(Ns[0] + 1):
        for n1 in range(Ns[1] + 1):
            for n2 in range(Ns[2] + 1):
                for n3 in range(Ns[3] + 1):
                    for h0 in range(S+1):
                        if n0 == n1 == n2 == n3 == 0:
                            continue

                        h1 = S-(n0+n1+n2+n3)

                        tmp = []
                        for k in range(1, 4):
                            if n0-k > 0:
                                d = dp[n0-k][n1][n2][n3][h1]
                            elif n0-k == 0:
                                d = dp[n0-k][n1][n2][n3][h1//2]
                            else:
                                break
                            tmp.append(d)

                        for k in range(1, 4):
                            if n1-k > 0:
                                d = dp[n0][n1-k][n2][n3][h1]
                            elif n1-k == 0:
                                d = dp[n0][n1-k][n2][n3][h1//2]
                            else:
                                break
                            tmp.append(d)

                        for k in range(1, 4):
                            if n2-k > 0:
                                d = dp[n0][n1][n2-k][n3][h1]
                            elif n2-k == 0:
                                d = dp[n0][n1][n2-k][n3][h1//2]
                            else:
                                break
                            tmp.append(d)

                        for k in range(1, 4):
                            if n3-k > 0:
                                d = dp[n0][n1][n2][n3-k][h1]
                            elif n3-k == 0:
                                d = dp[n0][n1][n2][n3-k][h1//2]
                            else:
                                break
                            tmp.append(d)

                        if -1 in tmp:
                            dp[n0][n1][n2][n3][h0] = 1
                        elif 0 not in tmp:
                            dp[n0][n1][n2][n3][h0] = -1
                        else:
                            dp[n0][n1][n2][n3][h0] = 0

                        # print(h0, h1, n0, n1, n2, n3, dp[n0][n1][n2][n3][h0])

    ans = dp[Ns[0]][Ns[1]][Ns[2]][Ns[3]][0]
    if ans == 1:
        print("Taro")
    elif ans == -1:
        print("Jiro")
    else:
        print("Draw")


if __name__ == "__main__":
    main()
