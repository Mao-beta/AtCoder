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
        # assert 0 <= p < self.n, "0<=p<n,p={0},n={1}".format(p, self.n)
        p += 1
        while (p <= self.n):
            self.data[p - 1] += x
            p += p & -p

    def get(self, p):
        return self.sum(p, p + 1)

    def sum(self, l, r):
        # assert (0 <= l and l <= r and r <= self.n), "0<=l<=r<=n,l={0},r={1},n={2}".format(l, r, self.n)
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


def main():
    N, M, K = NMI()
    A = NLI()
    B = sorted([[a, i] for i, a in enumerate(A)])
    V = [b for b, i in B]
    rem = K - sum(A)
    # print(sorted(A))
    # seg = BIT(N)
    # for i, v in enumerate(V):
    #     seg.add(i, v)

    C = list(accumulate([0] + V))
    # print(seg)
    ans = [0] * N

    if M == N:
        print(*ans)
        return

    for si in range(N):
        a, i = B[si]
        # print("#")
        # print(f"{a=} {i=} {si=}")
        def judge(X):
            # aに加えてX票取ったときにいけるか
            ax = a + X
            r = bisect.bisect_right(V, ax)
            if si < N-M:
                l = N-M
            else:
                l = N-M-1

            if l >= r:
                return False

            # [:r]まではa+X以下
            now = C[r] - C[l]
            num = r-l
            if l <= si < r:
                now -= a
                num -= 1
            add = (ax+1)*num - now
            # print(a, i, ax, l, r, now, num)
            return X + add > rem

        ok = 10**18
        ng = -1
        while abs(ok - ng) > 1:
            X = (ok + ng) // 2
            if judge(X):
                ok = X
            else:
                ng = X
        ans[i] = ok if ok <= rem else -1
        # print(f"{a=} {i=} {si=} {ok=}")
    print(*ans)


if __name__ == "__main__":
    main()
