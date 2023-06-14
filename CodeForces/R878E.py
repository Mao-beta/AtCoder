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


class RollingHashSingle():
    """
    文字列S(の各文字をintにしたもの)についてのHash
    文字列の長さは変わらない前提　全体のhashのみわかればいいとき
    文字の差し替えはできる
    # init
    rh = RollingHashSingle(S, 37, MOD)
    # rh.set(i, s): i文字目をsにする
    # rh.S: 文字列そのもの
    # rh.val: 文字列全体のhash
    """
    def __init__(self, S, base, mod):
        self.mod = mod
        self.pw = [1]*(len(S) + 1)
        self.S = S[:]

        self.l = len(S)
        self.h = h = [0]*(self.l+1)

        v = 0
        for i in range(self.l):
            h[i+1] = v = (v * base + S[i]) % mod
        v = 1
        for i in range(self.l):
            self.pw[i+1] = v = v * base % mod

        self.val = self.h[-1] % self.mod

    def hash_i(self, i):
        # i文字目のhash  全部足すとvalになる
        return self.S[i] * self.pw[self.l-1 - i] % self.mod

    def set(self, i, s):
        self.val -= self.hash_i(i)
        self.S[i] = s
        self.val += self.hash_i(i)
        self.val %= self.mod


alphabets = "abcdefghijklmnopqrstuvwxyz"
D = {s:i for i, s in enumerate(alphabets)}

def convert(S):
    return [D[s] for s in S]


def main():
    case = NI()
    for _ in range(case):
        S1 = convert(SI())
        S2 = convert(SI())
        T, Q = NMI()
        N = len(S1)
        # blockされている文字列
        B1 = [0] * N
        B2 = [0] * N
        # q回目のクエリ前に解放されるpos
        R = [[] for _ in range(Q+1)]

        base = 37
        MOD = 10**21
        hs1 = RollingHashSingle(S1, base, MOD)
        hs2 = RollingHashSingle(S2, base, MOD)
        hb1 = RollingHashSingle(B1, base, MOD)
        hb2 = RollingHashSingle(B2, base, MOD)
        # print(hs1.S)
        # print(hs2.S)

        for qi in range(Q):
            q, *X = NMI()
            # print(qi)
            for i in R[qi]:
                hb1.set(i, 0)
                hb2.set(i, 0)

            if q == 1:
                i = X[0] - 1
                hb1.set(i, hs1.S[i])
                hb2.set(i, hs2.S[i])
                if qi + T <= Q:
                    R[qi+T].append(i)

            elif q == 2:
                X = [x-1 for x in X]
                a, ai, b, bi = X
                hsa = [hs1, hs2][a]
                hsb = [hs1, hs2][b]
                sa = hsa.S[ai]
                sb = hsb.S[bi]
                hsa.set(ai, sb)
                hsb.set(bi, sa)

            else:
                # print((hs1.val, hb1.val), (hs2.val, hb2.val))
                # print((hs1.val - hb1.val), (hs2.val - hb2.val))
                if (hs1.val - hb1.val) % MOD == (hs2.val - hb2.val) % MOD:
                    print("YES")
                else:
                    print("NO")

            # print(hs1.S)
            # print(hs2.S)
            # print(hb1.S)
            # print(hb2.S)




if __name__ == "__main__":
    main()
