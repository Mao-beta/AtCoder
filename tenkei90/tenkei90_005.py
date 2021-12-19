import sys
import math
from collections import deque

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, B, K = NMI()
    C = NLI()

    # dp[i] 2^i回ぶんの遷移後のベクトル
    dp = [[0]*B for _ in range(61)]
    dp[0][0] = 1

    P10 = [1]
    for i in range(60):
        P10.append(P10[-1] * 10 % MOD)

    for i in range(1, 61):
        for j in range(B):
            for k in range(B):
                nj = (j * P10[i] + k) % MOD


if __name__ == "__main__":
    main()
