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


class segtree():
    n = 1
    size = 1
    log = 2
    d = [0]
    op = None
    e = 10 ** 15

    def __init__(self, V, OP, E):
        self.n = len(V)
        self.op = OP
        self.e = E
        self.log = (self.n - 1).bit_length()
        self.size = 1 << self.log
        self.d = [E for _ in range(2 * self.size)]
        for i in range(self.n):
            self.d[self.size + i] = V[i]
        for i in range(self.size - 1, 0, -1):
            self.update(i)

    def set(self, p, x):
        assert 0 <= p and p < self.n
        p += self.size
        self.d[p] = x
        for i in range(1, self.log + 1):
            self.update(p >> i)

    def get(self, p):
        assert 0 <= p and p < self.n
        return self.d[p + self.size]

    def prod(self, l, r):
        assert 0 <= l and l <= r and r <= self.n
        sml = self.e
        smr = self.e
        l += self.size
        r += self.size
        while l < r:
            if l & 1:
                sml = self.op(sml, self.d[l])
                l += 1
            if r & 1:
                smr = self.op(self.d[r - 1], smr)
                r -= 1
            l >>= 1
            r >>= 1
        return self.op(sml, smr)

    def all_prod(self):
        return self.d[1]

    def update(self, k):
        self.d[k] = self.op(self.d[2 * k], self.d[2 * k + 1])

    def __str__(self):
        return str([self.get(i) for i in range(self.n)])


# ------------------------------
# Node design for this problem
# ------------------------------
NEG_INF = -(1 << 60)

# Node = (
#   sumA_mod3, sumB,
#   pref0, pref1, pref2,   # best non-empty prefix with sumA ≡ r
#   suff0, suff1, suff2,   # best non-empty suffix  with sumA ≡ r
#   best0, best1, best2,   # best non-empty subarray with sumA ≡ r
# )

E_NODE = (0, 0,
          NEG_INF, NEG_INF, NEG_INF,
          NEG_INF, NEG_INF, NEG_INF,
          NEG_INF, NEG_INF, NEG_INF)

def make_leaf(a: int, b: int):
    # a in {0,1,2}
    if a == 0:
        return (0, b,
                b, NEG_INF, NEG_INF,
                b, NEG_INF, NEG_INF,
                b, NEG_INF, NEG_INF)
    elif a == 1:
        return (1, b,
                NEG_INF, b, NEG_INF,
                NEG_INF, b, NEG_INF,
                NEG_INF, b, NEG_INF)
    else:
        return (2, b,
                NEG_INF, NEG_INF, b,
                NEG_INF, NEG_INF, b,
                NEG_INF, NEG_INF, b)

def op(A, B):
    aA, aB, ap0, ap1, ap2, as0, as1, as2, ab0, ab1, ab2 = A
    bA, bB, bp0, bp1, bp2, bs0, bs1, bs2, bb0, bb1, bb2 = B

    sumA = (aA + bA) % 3
    sumB = aB + bB

    # pref[r] = max(prefL[r], sumB_L + prefR[(r - sumA_L) mod 3])
    if aA == 0:
        pref0 = max(ap0, aB + bp0)
        pref1 = max(ap1, aB + bp1)
        pref2 = max(ap2, aB + bp2)
    elif aA == 1:
        pref0 = max(ap0, aB + bp2)
        pref1 = max(ap1, aB + bp0)
        pref2 = max(ap2, aB + bp1)
    else:  # aA == 2
        pref0 = max(ap0, aB + bp1)
        pref1 = max(ap1, aB + bp2)
        pref2 = max(ap2, aB + bp0)

    # suff[r] = max(suffR[r], sumB_R + suffL[(r - sumA_R) mod 3])
    if bA == 0:
        suff0 = max(bs0, bB + as0)
        suff1 = max(bs1, bB + as1)
        suff2 = max(bs2, bB + as2)
    elif bA == 1:
        suff0 = max(bs0, bB + as2)
        suff1 = max(bs1, bB + as0)
        suff2 = max(bs2, bB + as1)
    else:  # bA == 2
        suff0 = max(bs0, bB + as1)
        suff1 = max(bs1, bB + as2)
        suff2 = max(bs2, bB + as0)

    # cross best:
    # r=0: max(as0+bp0, as1+bp2, as2+bp1)
    # r=1: max(as0+bp1, as1+bp0, as2+bp2)
    # r=2: max(as0+bp2, as1+bp1, as2+bp0)
    cross0 = max(as0 + bp0, as1 + bp2, as2 + bp1)
    cross1 = max(as0 + bp1, as1 + bp0, as2 + bp2)
    cross2 = max(as0 + bp2, as1 + bp1, as2 + bp0)

    best0 = max(ab0, bb0, cross0)
    best1 = max(ab1, bb1, cross1)
    best2 = max(ab2, bb2, cross2)

    return (sumA, sumB,
            pref0, pref1, pref2,
            suff0, suff1, suff2,
            best0, best1, best2)


def main():
    N, Q = NMI()
    A = NLI()
    B = NLI()

    V = [make_leaf(a, b) for a, b in zip(A, B)]
    seg = segtree(V, op, E_NODE)

    out = []
    for _ in range(Q):
        q = list(map(int, input().split()))
        t = q[0]
        if t == 1:
            p, x = q[1] - 1, q[2]
            A[p] = x
            seg.set(p, make_leaf(A[p], B[p]))
        elif t == 2:
            p, x = q[1] - 1, q[2]
            B[p] = x
            seg.set(p, make_leaf(A[p], B[p]))
        else:
            l, r, x = q[1] - 1, q[2], q[3]  # [l, r) に直す（元は [l+1, r]）
            node = seg.prod(l, r)
            ans = node[8 + x]  # best0,best1,best2 が index 8..10
            if ans <= NEG_INF // 2:
                out.append("No")
            else:
                out.append(str(ans))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
