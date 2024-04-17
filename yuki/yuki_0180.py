import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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



from collections import deque

class ConvexHullTrick():
    """
    追加する直線の傾きが単調減少、計算する x 座標が単調増加するときに、
    直線(y = ai*x + bi)の追加とmin_i f(x)を計算 O(N+Q)
    """
    def __init__(self):
        self.deq = deque()

    def check(self, f1, f2, f3):
        return (f2[0] - f1[0]) * (f3[1] - f2[1]) >= (f2[1] - f1[1]) * (f3[0] - f2[0])

    def f(self, f1, x):
        return f1[0] * x + f1[1]

    # add f_i(x)=a*x+b
    def add_line(self, a, b):
        f1 = (a, b)
        while len(self.deq) >= 2 and self.check(self.deq[-2], self.deq[-1], f1):
            self.deq.pop()
        self.deq.append(f1)

    # min f_i(x)
    def query(self, x):
        while len(self.deq) >= 2 and self.f(self.deq[0], x) >= self.f(self.deq[1], x):
            self.deq.popleft()
        return self.f(self.deq[0], x)


def main():
    N = NI()
    AB = EI(N)
    X = set()
    for i in range(N):
        for j in range(i+1, N):
            ai, bi = AB[i]
            aj, bj = AB[j]
            if bi == bj:
                continue
            # ai-aj + (bi-bj)x = 0
            x = (aj-ai) // (bi-bj)
            X.add(x-1)
            X.add(x)
            X.add(x+1)
    X = sorted(list(X))
    CHTmax = ConvexHullTrick()
    CHTmin = ConvexHullTrick()
    AB.sort(key=lambda x: -x[1])
    for a, b in AB:
        CHTmin.add_line(b, a)
    AB.sort(key=lambda x: x[1])
    for a, b in AB:
        CHTmax.add_line(-b, -a)

    m = 10**20
    ans = 1
    for x in X:
        if x <= 0:
            continue
        res = -CHTmax.query(x) - CHTmin.query(x)
        if res < m:
            ans = x
            m = min(m, res)
    print(ans)


if __name__ == "__main__":
    main()
