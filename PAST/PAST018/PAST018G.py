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


from typing import List
from itertools import groupby

# RUN LENGTH ENCODING str -> list(tuple())
# example) "aabbbbaaca" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)]
def runLengthEncode(S: str) -> "List[tuple[str, int]]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res


def main(N, A, B):
    if sorted(A) != sorted(B):
        return False
    bit = BIT(N)
    D = defaultdict(deque)
    for i, a in enumerate(A):
        D[a].append(i)

    num = 0
    for b in B:
        ai = D[b].popleft()
        num += bit.sum(ai, N)
        bit.add(ai, 1)
    # print("ans", num)
    if num == 0 or num == 2:
        return True
    elif num == 1:
        AR = runLengthEncode(A)
        BR = runLengthEncode(B)
        for x, k in AR + BR:
            if k > 1:
                return True
    return False


def guchoku(N, _A, _B):
    A = _A[:]
    B = _B[:]
    # print("start", A, B)
    for i in range(N-1):
        A[i], A[i+1] = A[i+1], A[i]
        # print(f"{i=} {A}")
        for j in range(N-1):
            A[j], A[j+1] = A[j+1], A[j]
            # print(f"{j=} {A}")
            if A == B:
                print("gu", i, j, A, B)
                return True
            A[j], A[j+1] = A[j+1], A[j]
        A[i], A[i+1] = A[i+1], A[i]
    return False


if __name__ == "__main__":
    N = NI()
    A = NLI()
    B = NLI()
    if main(N, A, B):
        print("Yes")
    else:
        print("No")
    exit()
    from random import randint, shuffle
    for _ in range(1000):
        N = 5
        A = [randint(1, N) for _ in range(N)]
        B = A[:]
        shuffle(B)
        print(A, B)
        ans = main(N, A, B)
        gu = guchoku(N, A, B)
        print(A, B, ans, gu)
        assert ans == gu
