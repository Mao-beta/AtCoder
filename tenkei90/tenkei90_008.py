import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    S = SI()
    A = "atcoder"

    # i文字まで見て、j/7文字目までできているときの通り
    dp = [[0]*(len(A)+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        s = S[i-1]
        for j in range(len(A)+1):
            dp[i][j] += dp[i-1][j]
            if j > 0 and A[j-1] == s:
                dp[i][j] += dp[i-1][j-1]
                dp[i][j] %= MOD

    print(dp[N][len(A)])


if __name__ == "__main__":
    main()
