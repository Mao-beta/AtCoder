import sys
import math
from collections import deque

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, X, Y = NMI()
    A = NLI()
    B = NLI()
    dp = [float("inf")] * (1<<N)
    dp[0] = 0

    for case in range((1<<N)-1):
        base_idx = bin(case).count("1")
        #print(case, base_idx)
        base = A[base_idx]

        BI = [-1] * N
        tmp = base_idx
        for i in range(N):
            if (case >> i) & 1:
                continue
            BI[i] = tmp
            tmp += 1

        for i in range(N):
            if (case>>i) & 1:
                continue
            new = case | (1<<i)
            #print(new)
            target = B[i]
            cost = Y * (BI[i] - base_idx) + X * abs(target - base)
            #print(cost)
            dp[new] = min(dp[new], dp[case] + cost)

    #print(dp)
    print(dp[-1])



if __name__ == "__main__":
    main()
