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
    A = [[[0]*102 for _ in range(102)] for _ in range(102)]

    for x in range(N):
        for y in range(N):
            a = NLI()
            A[x+1][y+1] = [0] + a[:] + [0] * (102-len(a))
    # for x in range(N+1):
    #     for y in range(N+1):
    #         print(x, y, A[x][y][:N+1])
    for x in range(N+1):
        for y in range(N+1):
            for z in range(N+1):
                if z > 0:
                    A[x][y][z] += A[x][y][z-1]
    for x in range(N+1):
        for z in range(N+1):
            for y in range(N+1):
                if y > 0:
                    A[x][y][z] += A[x][y-1][z]
    for z in range(N+1):
        for y in range(N+1):
            for x in range(N+1):
                if x > 0:
                    A[x][y][z] += A[x-1][y][z]
    # for x in range(N+1):
    #     for y in range(N+1):
    #         print(x, y, A[x][y][:N+1])
    Q = NI()
    for _ in range(Q):
        lx, rx, ly, ry, lz, rz = NMI()
        lx -= 1
        ly -= 1
        lz -= 1
        ans = A[rx][ry][rz] - (A[lx][ry][rz] + A[rx][ly][rz] + A[rx][ry][lz])\
         + (A[lx][ly][rz] + A[lx][ry][lz] + A[rx][ly][lz]) - A[lx][ly][lz]
        # print(A[rx][ry][rz], (A[lx][ry][rz] + A[rx][ly][rz] + A[rx][ry][lz]), (A[lx][ly][rz] + A[lx][ry][lz] + A[rx][ly][lz]), A[lx][ly][lz])
        print(ans)



if __name__ == "__main__":
    main()
