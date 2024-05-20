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


def main():
    N = NI()
    S = SI()
    dp = [[0]*10 for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        s = S[i]
        for j in range(10):
            if not dp[i][j]:
                continue
            if s != "?":
                dp[i+1][(j+int(s)*(i+1))%10] = 1
            else:
                for x in range(10):
                    dp[i+1][(j+x*(i+1))%10] = 1

    if dp[N][0]:
        print("Yes")
        S = list(S)
        nowj = 0
        for i in range(N-1, -1, -1):
            if S[i] != "?":
                nowj -= (i+1) * int(S[i])
                nowj %= 10
            else:
                for x in range(10):
                    nj = (nowj - (i+1) * x) % 10
                    if dp[i][nj]:
                        S[i] = str(x)
                        nowj = nj
                        break
        print("".join(S))

    else:
        print("No")


if __name__ == "__main__":
    main()
