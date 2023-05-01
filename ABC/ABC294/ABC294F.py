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
EI = lambda m: [NLI() for _ in range(m)]


def main():
    N, M, K = NMI()
    AB = EI(N)
    CD = EI(M)

    def judge(X):
        # 濃度X％以上の組がK個あるか？
        ABX = [100*a - X*(a+b) for a, b in AB]
        CDX = [100*c - X*(c+d) for c, d in CD]
        CDX.sort()
        cnt = 0
        for s in ABX:
            cnt += M - bisect.bisect_left(CDX, -s)
        return cnt >= K


    ok = 0
    ng = 101
    for _ in range(50):
        X = (ok + ng) / 2
        if judge(X):
            ok = X
        else:
            ng = X

    print(ok)


if __name__ == "__main__":
    main()
