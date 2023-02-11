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
    S = SI()
    X = NI()
    N = len(S)
    K = S.count("K")
    E = S.count("E")
    Y = S.count("Y")

    # Xが巨大なら余裕で全部できる
    M = N * (N-1) // 2
    if X >= M:
        fac = math.factorial
        ans = fac(N) // fac(K) // fac(E) // fac(Y)
        print(ans)
        return

    # dp[i][k][e][x]: i個決めて、そこまでにKがk個、Eがe個あり、x回交換しているときの種類数
    dp = [[[[0]*(X+1) for e in range(E+1)] for k in range(K+1)] for i in range(N+1)]
    dp[0][0][0][0] = 1

    for i in range(N):
        for k in range(min(K, i) + 1):
            ey = i - k
            for e in range(min(E, ey) + 1):
                y = ey - e
                if y > Y:
                    continue

                # 使ってないものをそのまま左に寄せる
                # 次のk/e/yを取ってくるのに何手かかるかを計算
                rem = []
                cnt_k = 0
                cnt_e = 0
                cnt_y = 0
                nk, ne, ny = -1, -1, -1

                for si, s in enumerate(S):
                    # 左に寄せている個数分だけ無視
                    if cnt_k < k and s == "K":
                        cnt_k += 1
                    elif cnt_e < e and s == "E":
                        cnt_e += 1
                    elif cnt_y < y and s == "Y":
                        cnt_y += 1
                    else:
                        if nk == -1 and s == "K":
                            nk = len(rem)
                        if ne == -1 and s == "E":
                            ne = len(rem)
                        if ny == -1 and s == "Y":
                            ny = len(rem)
                        rem.append(s)

                # 遷移
                for x in range(X+1):
                    d = dp[i][k][e][x]
                    if d == 0:
                        continue

                    if nk != -1 and x+nk <= X:
                        dp[i+1][k+1][e][x+nk] += d
                    if ne != -1 and x+ne <= X:
                        dp[i+1][k][e+1][x+ne] += d
                    if ny != -1 and x+ny <= X:
                        dp[i+1][k][e][x+ny] += d

    ans = sum(dp[-1][-1][-1])
    print(ans)


if __name__ == "__main__":
    main()
