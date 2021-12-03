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


import bisect
def LIS(A):
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
    A = NLI()
    L = LIS(A)
    R = LIS(A[::-1])[::-1]
    ans = 0
    for l, r in zip(L, R):
        ans = max(l+r-1, ans)
    print(ans)


if __name__ == "__main__":
    main()
