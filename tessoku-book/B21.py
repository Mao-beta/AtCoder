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


def LCS(S, T):
    """
    SとTの最長共通部分列 O(|S||T|)
    :param S:
    :param T:
    :return:LCSの長さ、LCSそのもの
    """
    N = len(S)
    M = len(T)
    dp = [[0]*(M+1) for _ in range(N+1)]
    for i in range(N+1):
        for j in range(M+1):
            x = dp[i][j]
            if i < N:
                dp[i+1][j] = max(dp[i+1][j], x)
            if j < M:
                dp[i][j+1] = max(dp[i][j+1], x)
            if i < N and j < M:
                dp[i+1][j+1] = max(dp[i+1][j+1], x + int(S[i] == T[j]))

    # 復元
    res = []
    i = N
    j = M
    while i > 0 or j > 0:
        d = dp[i][j]

        if i > 0 and dp[i-1][j] == d:
            i -= 1
            continue
        if j > 0 and dp[i][j-1] == d:
            j -= 1
            continue
        res.append(S[i-1])
        i -= 1
        j -= 1

    res = res[::-1]

    return len(res), "".join(res)


def main():
    N = NI()
    S = SI()
    T = S[::-1]

    print(LCS(S, T)[0])


if __name__ == "__main__":
    main()
