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


def print_err(*args):
    print(*args, file=sys.stderr)


class RollingHash():
    """
    文字列SについてのHash table
    rh = RollingHash(S, 37, MOD)
    hash = rh.get(l, r) # S[l:r]のhash
    """
    def __init__(self, s, base, mod):
        self.mod = mod
        self.pw = pw = [1]*(len(s)+1)

        l = len(s)
        self.h = h = [0]*(l+1)

        v = 0
        for i in range(l):
            h[i+1] = v = (v * base + ord(s[i])) % mod
        v = 1
        for i in range(l):
            pw[i+1] = v = v * base % mod

    def get(self, l, r):
        return (self.h[r] - self.h[l] * self.pw[r-l]) % self.mod


def main():
    N = NI()
    T = SI()
    R = T[::-1]
    rh_t = RollingHash(T, 37, MOD99)
    rh_r = RollingHash(R, 37, MOD99)
    for l in range(N+1):
        S1 = rh_r.get(N-l, 2*N-l)
        S2 = (rh_t.get(0, l) * rh_t.pw[N-l] + rh_t.get(l+N, 2*N)) % rh_t.mod
        if S1 == S2:
            print(T[:l] + T[l+N:])
            print(l)
            exit()
    print(-1)


if __name__ == "__main__":
    main()
