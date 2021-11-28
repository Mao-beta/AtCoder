import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    A, B = NMI()

    def solve(N):
        N = str(N)
        K = len(N)
        # dp[i][j]
        # i桁まで確定(0<=i<=K) N未満のときj==1 4か9使っているときk==1
        dp = [[[0]*2 for _ in range(2)] for _ in range(K+1)]
        dp[0][0][0] = 1

        for i in range(K):
            for j in range(2):
                for k in range(2):
                    lim = int(N[i]) if j == 0 else 9
                    for x in range(lim+1):
                        nj = j | (x < lim)
                        nk = k | (x == 4) | (x == 9)
                        dp[i+1][nj][nk] += dp[i][j][k]

        return dp[K][0][1] + dp[K][1][1]

    print(solve(B) - solve(A-1))



if __name__ == "__main__":
    main()
