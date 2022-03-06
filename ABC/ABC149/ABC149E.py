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
    N, M = NMI()
    A = NLI()
    A.sort()
    cum = list(accumulate([0]+A))

    # M　>= N**2 のとき必ずできる
    if M >= N**2:
        print(cum[-1]*2*N)
        exit()

    # Ax+Ay がX以上のものだけ行うとき、M回以下にできるか？
    ok = 10**20
    ng = 0
    ok_cnt = 0
    ok_sum = 0

    while abs(ok-ng) > 1:
        X = (ok+ng) // 2
        # print(X)
        cnt = 0
        S = 0

        for a in A:
            rem = X - a
            cant = bisect.bisect_left(A, rem)
            can = N - cant
            cnt += can
            S += a * can + cum[-1] - cum[cant]

        if cnt <= M:
            # print("ok", cnt, S)
            ok = X
            ok_cnt = cnt
            ok_sum = S
        else:
            # print("ng", cnt, S)
            ng = X

    rem_cnt = M - ok_cnt
    ans = ok_sum + ng * rem_cnt
    print(ans)


if __name__ == "__main__":
    main()
