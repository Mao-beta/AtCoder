import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    N = NI()
    S = SI()
    X = SI()
    dp = [[0]*7 for _ in range(N+1)]
    dp[N][0] = 1
    for i in range(N, 0, -1):
        s = int(S[i-1])
        if X[i-1] == "T":
            for k in range(7):
                dp[i-1][k] = dp[i][10*k%7] or dp[i][(10*k+s)%7]
        else:
            for k in range(7):
                dp[i-1][k] = dp[i][10*k%7] and dp[i][(10*k+s)%7]
    print("Takahashi" if dp[0][0] else "Aoki")



if __name__ == "__main__":
    main()
