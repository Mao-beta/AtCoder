import sys
import math
from collections import deque
from itertools import accumulate

sys.setrecursionlimit(100000)
MOD = 998244353
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    A = NLI()
    B = NLI()

    dp = [0] * 3001
    dp[0] = 1

    for i in range(N):
        now = dp.copy()
        L = [0] * 3002
        a, b = A[i], B[i]
        for j in range(3001):
            l = max(j, a)
            r = b
            if l > r: continue
            #print(j, l, r, now[j])
            L[l] += now[j]
            L[r+1] -= now[j]
        dp = list(accumulate(L))
        dp = [x % MOD for x in dp]

    print(sum(dp) % MOD)


if __name__ == "__main__":
    main()
