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
    S = SI()
    R = S[::-1]
    sh = RollingHash(S, 37, MOD99)
    rh = RollingHash(R, 37, MOD99)
    for i in range(N+1):
        r = rh.get(N-i, 2*N-i)
        sl = sh.get(0, i) * sh.pw[N-i] % sh.mod
        sr = sh.get(i+N, 2*N)
        s = (sl + sr) % sh.mod
        if s == r:
            print(R[N-i:2*N-i])
            print(i)
            return
    print(-1)


if __name__ == "__main__":
    main()
