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


def LIS(A):
    """
    A[:i]までに関するLISの長さのリストを取得する
    ans[i]はA[0:i+1]におけるLISの長さ
    """
    INF = 1<<60
    n = len(A)
    # dp[i]は長さがiとなるLISの末尾の最小値
    dp = [INF] * (n+1)
    dp[0] = -INF
    ans = []
    for a in A:
        idx = bisect.bisect_left(dp, a)
        dp[idx] = a
        ans.append(bisect.bisect_left(dp, INF) - 1)
    return ans


def main():
    N = NI()
    P = NLI()
    Q = NLI()
    Q_inv = {q:i for i, q in enumerate(Q)}

    B = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(i, N+1, i):
            B[i].append(Q_inv[j])
        B[i].sort(reverse=True)

    A = []
    for p in P:
        A += B[p]
    ans = LIS(A)
    print(ans[-1])


if __name__ == "__main__":
    main()
