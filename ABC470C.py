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
    A = [0] * N
    idx = []
    ans = 0
    for _ in range(Q):
        q, *x = NMI()
        if q == 1:
            x = x[0]-1
            ans ^= A[x]
            A[x] += 1
            ans ^= A[x]
            if A[x] == 1:
                idx.append(x)
        else:
            for i in idx:
                ans ^= A[i]
                A[i] -= 1
                ans ^= A[i]
            idx = [i for i in idx if A[i] > 0]
        print(ans)


if __name__ == "__main__":
    main()
