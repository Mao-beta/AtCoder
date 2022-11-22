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


def subset_sum_dp(A, S):
    """
    Aから0個以上選んで合計Sにできるか O(len(A)*S)
    :return: dp[i][j]: i番目まで見て合計jにできるか？のdp
    """
    N = len(A)
    dp = [[0]*(S+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        a = A[i]
        for j in range(S+1):
            dp[i+1][j] |= dp[i][j]
            if j+a <= S:
                dp[i+1][j+a] |= dp[i][j]
    return dp


def main():
    N, S = NMI()
    A = NLI()
    dp = subset_sum_dp(A, S)

    if dp[-1][S] == 0:
        print(-1)
        exit()

    nowS = S
    ans = []
    for i in range(N-1, -1, -1):
        a = A[i]
        if nowS < a:
            continue
        if dp[i][nowS - a]:
            nowS -= a
            ans.append(i+1)

    print(len(ans))
    print(*ans[::-1])


if __name__ == "__main__":
    main()
