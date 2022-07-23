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
    N, C = NMI()
    TA = [NLI() for _ in range(N)]
    B = 32
    # 最初がi=0/1で下からj bitめで連続k回操作後の値
    D = [[[0]*(N+1) for _ in range(B)] for _ in range(2)]

    for j in range(B):
        for i in range(2):
            c = i
            D[i][j][0] = c
            for k, (t, a) in enumerate(TA):
                if t == 1:
                    c &= (a >> j) & 1
                elif t == 2:
                    c |= (a >> j) & 1
                else:
                    c ^= (a >> j) & 1
                D[i][j][k+1] = c

    for k, (t, a) in enumerate(TA, start=1):
        ans = 0
        for j in range(B):
            i = (C >> j) & 1
            ans |= (D[i][j][k] << j)
        print(ans)
        C = ans


if __name__ == "__main__":
    main()
