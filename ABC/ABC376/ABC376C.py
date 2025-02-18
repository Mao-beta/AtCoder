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
    N = NI()
    A = NLI()
    A.sort()
    B = NLI()

    def judge(X):
        BX = sorted(B + [X])
        for a, b in zip(A, BX):
            if a > b:
                return False
        return True

    INF = 10**15
    ok = INF
    ng = 0
    while abs(ok - ng) > 1:
        X = (ok + ng) // 2
        if judge(X):
            ok = X
        else:
            ng = X

    if ok == INF:
        BX = sorted(B + [ok])
        for a, b in zip(A, BX):
            if a > b:
                print(-1)
                exit()
    print(ok)


if __name__ == "__main__":
    main()
