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


def levenshtein(s1, s2):
    n, m = len(s1), len(s2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i

    for j in range(m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = dp[i - 1][j - 1] + cost  # replacement

    return dp[n][m]


def main():
    S = SI()
    T = SI()
    ans = 10**200
    for i in range(len(S)-len(T)+1):
        ss = S[i:i+len(T)]
        ans = min(ans, levenshtein(ss, T))
    print(ans)

if __name__ == "__main__":
    main()
