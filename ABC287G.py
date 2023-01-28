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


class BIT():
    """
    BIT 0-index  ACL for python
    add(p, x): p番目にxを加算
    get(p): p番目を取得
    sum0(r): [0:r)の和を取得
    sum(l, r): [l:r)の和を取得
    """

    def __init__(self, N):
        self.n = N
        self.data = [0 for i in range(N)]

    def add(self, p, x):
        assert 0 <= p < self.n, "0<=p<n,p={0},n={1}".format(p, self.n)
        p += 1
        while (p <= self.n):
            self.data[p - 1] += x
            p += p & -p

    def get(self, p):
        return self.sum(p, p + 1)

    def sum(self, l, r):
        assert (0 <= l and l <= r and r <= self.n), "0<=l<=r<=n,l={0},r={1},n={2}".format(l, r, self.n)
        return self.sum0(r) - self.sum0(l)

    def sum0(self, r):
        s = 0
        while (r > 0):
            s += self.data[r - 1]
            r -= r & -r
        return s

    def debug(self):
        res = [self.get(p) for p in range(self.n)]
        return res


def compress(S):
    """ 座標圧縮 """

    S = set(S)
    zipped, unzipped = {}, {}
    for i, a in enumerate(sorted(S)):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped


def main():
    N = NI()

    A = []
    B = []
    nums = [0] * N
    points = [0] * N

    for i in range(N):
        a, b = NMI()
        A.append(a)
        B.append(b)
        points[i] = a
        nums[i] = b

    Q = NI()
    querys = EI(Q)
    Y1 = [X[-1] for q, *X in querys if q == 1]
    # print(Y1)

    ZA, UZA = compress(A+Y1)
    # print(A+Y1)
    # print(ZA)
    M = len(ZA)
    # 座圧後得点→枚数を得る
    bit = BIT(M)
    bits = BIT(M)

    for i, (a, b) in enumerate(zip(A, B)):
        za = ZA[a]
        bit.add(za, b)
        bits.add(za, a*b)

    # print(bit.debug())
    # print(bits.debug())

    for query in querys:
        q, *X = query
        # print(*query)
        if q == 1:
            x, new_p = X
            x -= 1
            old_p = points[x]
            old_pz = ZA[old_p]
            new_pz = ZA[new_p]
            bit.add(old_pz, -nums[x])
            bit.add(new_pz, nums[x])
            bits.add(old_pz, -nums[x]*old_p)
            bits.add(new_pz, nums[x]*new_p)
            points[x] = new_p

        elif q == 2:
            x, new_num = X
            x -= 1
            p = points[x]
            pz = ZA[p]
            # print(p, pz, -nums[x], new_num)
            bit.add(pz, -nums[x])
            bit.add(pz, new_num)
            bits.add(pz, -nums[x]*points[x])
            bits.add(pz, new_num*points[x])
            nums[x] = new_num

        else:
            x = X[0]

            if bit.sum(0, M) < x:
                print(-1)
            else:
                # 左端を二分探索
                ok = 0
                ng = M
                while abs(ok-ng) > 1:
                    mid = (ok + ng) // 2
                    if bit.sum(mid, M) >= x:
                        ok = mid
                    else:
                        ng = mid

                ans = bits.sum(ng, M) + UZA[ok] * (x - bit.sum(ng, M))
                print(ans)

        # print("nums", nums)
        # print("points", points)
        # print(bit.debug())
        # print(bits.debug())


if __name__ == "__main__":
    main()
