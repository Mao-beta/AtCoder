import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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
EI = lambda m: [NLI() for _ in range(m)]


import bisect
def LIS(A):
    """
    A[:i]までに関するLISの長さのリストを取得する
    ans[i]はA[0:i]におけるLISの長さ
    """
    INF = 1<<60
    n = len(A)
    # dp[i]は長さがiとなるLISの末尾の最小値
    dp = [INF] * (n+1)
    dp[0] = -INF
    ans = [0]
    dp2 = [0] * n
    for i, a in enumerate(A):
        idx = bisect.bisect_left(dp, a)
        dp[idx] = a
        dp2[i] = idx
        ans.append(bisect.bisect_left(dp, INF) - 1)
    return ans[-1], dp2



def main():
    T = NI()
    for _ in range(T):
        N = NI()
        A = NLI()
        L, left = LIS(A)
        right = LIS([-a for a in A[::-1]])[1][::-1]
        ans = []
        for i in range(N):
            if left[i] + right[i] == L+1:
                ans.append(i+1)
        print(len(ans))
        print(*ans)


if __name__ == "__main__":
    main()
