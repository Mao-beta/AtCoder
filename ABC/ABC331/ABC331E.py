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
    N, M, L = NMI()
    A = NLI()
    B = NLI()
    CD = EI(L)
    CD = [[x-1, y-1] for x, y in CD]
    Bad = [A[c] + B[d] for c, d in CD]
    Bad.sort()
    SA = sorted(A)
    SB = sorted(B)

    def judge(X):
        # 合計X以上の定食が存在するか？
        num = 0
        for a in SA:
            # X-a以上の副菜
            num += M - bisect.bisect_left(SB, X-a)
        bad = L - bisect.bisect_left(Bad, X)
        return num - bad > 0

    ok = 0
    ng = 10**10
    while abs(ok - ng) > 1:
        X = (ok + ng) // 2
        if judge(X):
            ok = X
        else:
            ng = X

    print(ok)


if __name__ == "__main__":
    main()
