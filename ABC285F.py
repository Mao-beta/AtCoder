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


def main():
    N = NI()
    S = list(SI())
    Q = NI()
    S = [ord(s) - ord("a") for s in S]

    # S[i] > S[i+1]なら1
    # desc.sum(l, r-1) > 0: [l, r)に逆順が存在するか？
    desc = BIT(N)
    # C[s]: BIT p番目が文字sなら1
    # C[s].sum(l, r)で個数を取得し、Tと比較
    C = [BIT(N) for _ in range(26)]

    T = Counter(S)

    for i, s in enumerate(S):
        C[s].add(i, 1)
        if i < N-1 and s > S[i+1]:
            desc.add(i, 1)


    for _ in range(Q):
        query = SLI()
        # print(query)

        if query[0] == "1":
            x, c = query[1:]
            x = int(x)
            x -= 1
            c = ord(c) - ord("a")
            s = S[x]
            T[s] -= 1
            T[c] += 1
            S[x] = c

            C[s].add(x, -1)
            C[c].add(x, 1)

            if x > 0:
                desc.add(x-1, -desc.get(x-1))
                if S[x-1] > S[x]:
                    desc.add(x-1, 1)
            if x < N-1:
                desc.add(x, -desc.get(x))
                if S[x] > S[x+1]:
                    desc.add(x, 1)

        else:
            l, r = query[1:]
            l, r = int(l), int(r)
            l -= 1
            if r - l == 1:
                print("Yes")
                continue

            if desc.sum(l, r-1) > 0:
                print("No")
                continue

            X = [0] * 26
            for s in range(26):
                X[s] = C[s].sum(l, r)

            start = False
            end = False
            ok = True
            for s in range(26):
                if not start and X[s] == 0:
                    continue
                if X[s] > T[s]:
                    ok = False
                    break

                if end and X[s] > 0:
                    ok = False
                    break
                elif end:
                    continue

                if start:
                    if X[s] < T[s]:
                        end = True
                        continue
                else:
                    if X[s] <= T[s]:
                        start = True

            if ok:
                print("Yes")
            else:
                print("No")


        # print(desc.debug())
        #
        # for s in range(26):
        #     print(C[s].debug())


if __name__ == "__main__":
    main()
