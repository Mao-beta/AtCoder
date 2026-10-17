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
    N, M, T = NMI()
    A = NLI()
    XY = EI(M)
    B = [0] * N
    for x, y in XY:
        B[x-1] += y
    for i in range(N-1):
        T += B[i]
        if T <= A[i]:
            print("No")
            return
        T -= A[i]
    print("Yes")


if __name__ == "__main__":
    main()
