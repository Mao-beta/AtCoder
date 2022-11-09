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
    N = 20
    T = NI()
    PQR = [NLI() for _ in range(T)]
    PQR = [[p-1, q-1, r-1] for p, q, r in PQR]

    X = [0] * N


    def add_k(p, q, r, k):
        X[p] += k
        X[q] += k
        X[r] += k

    def count_zero():
        return X.count(0)


    def abs_error():
        return sum([abs(x) for x in X])


    score = 0
    ans = []
    for pqr in PQR:
        add_k(*pqr, 1)
        error_a = abs_error()
        new_a = count_zero()
        add_k(*pqr, -2)
        error_b = abs_error()
        new_b = count_zero()

        if error_a < error_b:
            add_k(*pqr, 2)
            score += new_a
            ans.append("A")
        else:
            score += new_b
            ans.append("B")

        # print(score)
        # print(X)

    print("\n".join(ans))


if __name__ == "__main__":
    main()
