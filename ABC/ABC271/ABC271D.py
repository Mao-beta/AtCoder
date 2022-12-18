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


def main():
    N, S = NMI()
    AB = [NLI() for _ in range(N)]
    dp = [[0]*(S+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        a, b = AB[i]
        for s in range(S):
            if s+a <= S:
                dp[i+1][s+a] |= dp[i][s]
            if s+b <= S:
                dp[i+1][s+b] |= dp[i][s]

    # print(*dp, sep="\n")
    if dp[-1][S]:
        print("Yes")
        ans = []
        now = N
        s = S
        while now > 0:
            now -= 1
            a, b = AB[now]
            if dp[now][s-a]:
                s -= a
                ans.append("H")
            else:
                s -= b
                ans.append("T")
        print("".join(ans[::-1]))

    else:
        print("No")


if __name__ == "__main__":
    main()
