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
    N, M = NMI()
    AB = EI(M)
    AB = [[x-1, y-1] for x, y in AB]

    def f(i, j):
        return N*i+j

    def g(ij):
        return divmod(ij, N)

    yoko = set()
    tate = set()
    kesa = set()
    gyak = set()
    for a, b in AB:
        yoko.add(a)
        tate.add(b)
        kesa.add(a+b)
        gyak.add(a-b)
    C = Counter()
    for x in yoko:
        for y in tate:
            C[f(x, y)] += 1
    for x in yoko:
        for y in kesa:
            if 0 <= y-x < N:
                C[f(x, y-x)] += 1
    for x in yoko:
        for y in gyak:
            if 0 <= x-y < N:
                C[f(x, x-y)] += 1
    for x in tate:
        for y in kesa:
            if 0 <= y-x < N:
                C[f(y-x, x)] += 1
    for x in tate:
        for y in gyak:
            if 0 <= y+x < N:
                C[f(y+x, x)] += 1
    for x in kesa:
        for y in gyak:
            if (x+y) % 2 or (x-y) % 2:
                continue
            if 0 <= (x+y)//2 < N and 0 <= (x-y)//2 < N:
                C[f((x+y)//2, (x-y)//2)] += 1

    kesa_tmp = 0
    for x in kesa:
        if x >= N:
            x = 2*(N-1) - x
        kesa_tmp += x+1

    gyak_tmp = 0
    for x in gyak:
        if x < 0:
            x *= -1
        gyak_tmp += N-x

    base = len(tate) * N + len(yoko) * N + kesa_tmp + gyak_tmp
    dup = 0
    for ij, k in C.items():
        if k == 1:
            dup += 1
        elif k == 3:
            dup += 2
        elif k == 6:
            dup += 3
    print(N**2 - base + dup)


if __name__ == "__main__":
    main()
