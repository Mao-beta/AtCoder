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
    N, K = NMI()
    S = SI()

    dp = [[-1]*26 for _ in range(N+1)]
    for i in range(N-1, -1, -1):
        s = S[i]
        sn = ord(s) - ord("a")
        for j in range(26):
            if j == sn:
                dp[i][j] = i
            else:
                dp[i][j] = dp[i+1][j]

    now = 0
    ans = []
    for i in range(K):
        letters = dp[now]
        for j, l_idx in enumerate(letters):
            if l_idx == -1: continue
            if K - i <= N - l_idx:
                s = chr(j + ord("a"))
                ans.append(s)
                now = l_idx + 1
                break
    print("".join(ans))


if __name__ == "__main__":
    main()
