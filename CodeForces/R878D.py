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
    T = NI()
    for _ in range(T):
        N = NI()
        A = NLI()
        A.sort()

        def judge(X):
            idx = 0
            for _ in range(3):
                l = A[idx]
                r = l + X*2
                nidx = bisect.bisect_right(A, r)
                if nidx >= N:
                    return True
                idx = nidx

            return False

        ok = 10**9
        ng = -1
        while abs(ok - ng) > 1:
            X = (ok + ng) // 2
            if judge(X):
                ok = X
            else:
                ng = X

        print(ok)


if __name__ == "__main__":
    main()
