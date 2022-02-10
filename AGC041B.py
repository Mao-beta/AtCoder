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
    N, M, V, P = NMI()
    A = NLI()
    A.sort()

    def judge(x):
        # x点の問題が選ばれうるか？

        # x+M点より高いのがP問以上あれば無理
        over = N - bisect.bisect_left(A, x+M+1)
        if over >= P:
            return False

        # x点以下の問題と上からP-1問にはM票入れてよい
        nx = bisect.bisect_right(A, x)
        v = V - nx - (P-1)
        if v <= 0:
            return True

        s = sum(A[nx: N-(P-1)])
        # print(x, s, M, v)
        if s + M * v <= (x + M) * (N-P+1-nx):
            return True
        else:
            return False

    ok = max(A)
    ng = -1
    # print(A)

    while abs(ok - ng) > 1:
        X = (ok + ng) // 2
        j = judge(X)
        # print(X, j, ok, ng)
        if j:
            ok = X
        else:
            ng = X

    print(N - bisect.bisect_left(A, ok))


if __name__ == "__main__":
    main()
