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
    A = sorted(NLI())
    ans = []
    B = A[:]
    L = B[-1]
    while B and B[-1] == L:
        B.pop()
    BN = len(B)
    if BN % 2 == 0:
        ok = True
        for i in range(BN):
            if B[i] + B[BN-1-i] != L:
                ok = False
        if ok:
            ans.append(L)
    if N % 2 == 0:
        ok = True
        for i in range(N):
            if A[i] + A[N - 1 - i] != A[0] + A[-1]:
                ok = False
        if ok:
            ans.append(A[0] + A[-1])
    print(*ans)


if __name__ == "__main__":
    main()
