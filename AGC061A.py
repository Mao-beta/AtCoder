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


def get_msb(v):
    v |= (v >> 1)
    v |= (v >> 2)
    v |= (v >> 4)
    v |= (v >> 8)
    v |= (v >> 16)
    v |= (v >> 32)
    return 1 << (bin(v).count("1") - 1)

def solve(N, K, start):
    msb = get_msb(N)
    add = N - msb

    if add == 0:
        if K % 2 == 0:
            return start + K - 1 - 1
        else:
            return start + K - 1 + 1

    if add == 1:
        if K == 1:
            return start + 1
        if K == N-1:
            return start + N - 1
        if K % 2 == 0:
            return start + K - 1 + 2
        else:
            return start + K - 1 - 2

    rem = N - add * 2
    # add1 rem add2
    add1_l = start
    rem_l = add1_l + add
    add2_l = rem_l + rem
    # print(add1_l, rem_l, add2_l)

    target = start + K - 1
    if target < rem_l:
        return solve(add, K, add1_l)
    elif target < add2_l:
        return target
    else:
        return solve(add, K - add - rem, add2_l)


def guchoku(N, K):
    A = list(range(N+1))
    moto = A[:]

    def rec(L, R):
        if R <= L+1:
            A[L], A[R] = A[R], A[L]
            return
        rec(L, R-1)
        rec(L+1, R)

    rec(1, N)
    print(N, "guchoku")
    print(moto[1:])
    print(A[1:])


def main():
    T = NI()
    for t in range(1, T+1):
        N, K = NMI()
        ans = solve(N, K, 1)
        print(ans)
        # N, K = t, 0
        # guchoku(N, K)


if __name__ == "__main__":
    main()
