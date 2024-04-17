import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
    N, Pa, Pb = SMI()
    N = int(N)
    Pa = float(Pa)
    Pb = float(Pb)
    A = NLI()
    B = NLI()
    A.sort()
    B.sort()

    def f(p):
        # dp[i][j]: Xiがjターン目に出される確率
        dp = [[0]*N for _ in range(N)]
        # P[case]: caseに到達する確率
        P = [0] * (1<<N)
        P[0] = 1

        for case in range(1<<N):
            turn = case.bit_count()
            first = True
            # print("#", bin(case))
            for i in range(N):
                if (case >> i) & 1:
                    continue
                if turn == N-1:
                    dp[i][turn] += P[case]
                    P[case|(1<<i)] += P[case]
                elif first:
                    # print(i, p, p)
                    dp[i][turn] += P[case] * p
                    P[case|(1<<i)] += P[case] * p
                    first = False
                else:
                    # print(i, (1-p) / (N-1-turn), (1-p))
                    dp[i][turn] += P[case] * (1-p) / (N-1-turn)
                    P[case|(1<<i)] = P[case] * (1-p) / (N-1-turn)

        return dp

    dpa = f(Pa)
    dpb = f(Pb)

    ans = 0
    for turn in range(N):
        s = 0
        for ai in range(N):
            for bi in range(N):
                s += dpa[ai][turn] * dpb[bi][turn]
                if A[ai] > B[bi]:
                    # print(A[ai], B[bi], turn, dpa[ai][turn], dpb[bi][turn])
                    ans += (A[ai]+B[bi]) * dpa[ai][turn] * dpb[bi][turn]

        print(s)
    print(ans)


if __name__ == "__main__":
    main()
