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
    S = ""
    for i in range(4):
        S += SI()

    def hit(case, i):
        h, w = divmod(i, 4)
        DH = [0, 0, 0, -1, 1]
        DW = [0, 1, -1, 0, 0]
        A = []
        for dh, dw in zip(DH, DW):
            nh = h + dh
            nw = w + dw
            if 0 <= nh < 4 and 0 <= nw < 4:
                ni = nh * 4 + nw
                if (case >> ni) & 1:
                    A.append(case ^ (1 << ni))

        return A

    start = 0
    for i in range(16):
        if S[i] == "#":
            start += 1 << i

    C = []
    case = start
    while case > 0:
        C.append(case)
        case = (case - 1) & start

    C = C[::-1]
    INF = 10**20
    dp = [INF] * (1<<16)
    dp[0] = 0

    for case in C:
        res = INF

        for h in range(4):
            for w in range(4):
                i = h * 4 + w
                A = hit(case, i)
                num = len(A)
                if num == 0:
                    continue

                tmp = 1
                for a in A:
                    tmp += dp[a] / 5
                tmp = tmp * 5 / num
                res = min(res, tmp)

        dp[case] = res

    print(dp[start])


if __name__ == "__main__":
    main()
