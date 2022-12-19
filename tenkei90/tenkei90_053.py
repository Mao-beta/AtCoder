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
    N = NI()

    F = 1597
    # F = 8
    A = [-i for i in range(1, F + 2)]

    ans = [0]

    def ask(idx):
        print(f"? {idx+1}")
        sys.stdout.flush()

        a = NI()
        assert a != -1
        A[idx] = a
        ans[0] = max(ans[0], a)
        return a


    def get_or_ask(idx):
        if idx >= N:
            return A[idx]

        if A[idx] < 0:
            return ask(idx)
        else:
            return A[idx]


    def rec(l, r, g):
        ml = r - g
        mr = l + g
        if not l < ml < mr < r:
            print(f"! {ans[0]}")
            sys.stdout.flush()

        # print(l, ml, mr, r)
        aml = get_or_ask(ml)
        amr = get_or_ask(mr)

        if aml < amr:
            rec(ml, r, r-l-g)
        else:
            rec(l, mr, r-l-g)

    rec(0, 1597, 987)
    # rec(0, 8, 5)


def guchoku():
    N = NI()

    def ask(idx):
        print(f"? {idx+1}")
        sys.stdout.flush()
        a = NI()
        assert a != -1
        return a

    ans = 0
    for i in range(N):
        a = ask(i)
        ans = max(ans, a)
    print(f"! {ans}")
    sys.stdout.flush()


if __name__ == "__main__":
    T = NI()
    for _ in range(T):
        # guchoku()
        main()
    exit()