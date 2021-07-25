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


def main():
    N, S = NMI()
    AB = [NLI() for _ in range(N)]

    dp = [[0]*(S+1) for _ in range(N+1)]
    dp[0][0] = 1

    for i, (a, b) in enumerate(AB, start=1):
        for j in range(S+1):
            if j >= a:
                dp[i][j] |= dp[i-1][j-a]
            if j >= b:
                dp[i][j] |= dp[i-1][j-b]


    if not dp[N][S]:
        print("Impossible")
        exit()


    def rec(now, ans):
        if now == 0:
            print(ans[::-1])
            exit()

        i = N-1 - len(ans)
        a, b = AB[i]

        if now >= a and dp[i][now-a]:
            rec(now-a, ans + "A")
        if now >= b and dp[i][now-b]:
            rec(now-b, ans + "B")


    rec(S, "")


if __name__ == "__main__":
    main()
