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
    N, Q = NMI()
    A = sorted(NLI())
    BK = [NLI()+[i] for i in range(Q)]
    BK.sort()
    ans = [0] * Q
    border = 0
    INF = 10**9
    for b, k, i in BK:
        while border < N and A[border] < b:
            border += 1

        # 距離X以下にK個以上あるか？
        def judge(X):
            res = bisect.bisect_right(A, b+X) - bisect.bisect_left(A, b-X)
            return res >= k

        ok = 10**9
        ng = -1
        while abs(ok - ng) > 1:
            X = (ok + ng) // 2
            if judge(X):
                ok = X
            else:
                ng = X

        ans[i] = ok

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
