import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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

    def query(x, y):
        print(f"1 {x} {y}", flush=True)
        return NI()

    def judge(X):
        d1 = query(X, 0)
        d2 = query(X+1, 0)
        return d1 <= d2

    ng = -10**8-1
    ok = 10**8+1
    while abs(ok - ng) > 1:
        X = (ok + ng) // 2
        if judge(X):
            ok = X
        else:
            ng = X

    def judge2(Y):
        d1 = query(0, Y)
        d2 = query(0, Y+1)
        return d1 <= d2

    ng2 = -10 ** 8 - 1
    ok2 = 10 ** 8 + 1
    while abs(ok2 - ng2) > 1:
        X = (ok2 + ng2) // 2
        if judge2(X):
            ok2 = X
        else:
            ng2 = X

    print(f"2 {ok} {ok2}")


if __name__ == "__main__":
    main()
