import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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



xor128_x = 123456789
xor128_y = 362436069
xor128_z = 521288629
xor128_w = 88675123

mask = (1 << 32) - 1

def xor128():
    global xor128_x, xor128_y, xor128_z, xor128_w
    t = xor128_x ^ (xor128_x << 11)
    t &= mask
    xor128_x, xor128_y, xor128_z = xor128_y, xor128_z, xor128_w
    xor128_w = xor128_w ^ (xor128_w >> 19) ^ (t ^ (t >> 8))
    xor128_w &= mask
    return xor128_w

def generateA(N):
    A = []
    for i in range(N):
        A.append(xor128() % 100003)
    return A


def main():
    N, Q = NMI()
    M = 100003
    A = generateA(N)
    cutoff = 3000
    if N <= 3000:
        for _ in range(Q):
            q = NI()
            B = [a*q % M for a in A]
            print(max(B))
    else:
        SA = set(A)
        for _ in range(Q):
            q = NI()
            if q == 0:
                print(0)
                continue
            inv = pow(q, M-2, M)
            for x in range(M-1, M-1-3000, -1):
                a = x * inv % M
                if a in SA:
                    print(x)
                    break


if __name__ == "__main__":
    main()
