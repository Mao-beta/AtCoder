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


# 削除可能heapq
from heapq import *
class Heapq:
    '''
    Heapq()    : 本体qと削除用pの2本のheapqを用意する
    build(a)   : 配列aからプライオリティキューqを構築する
    push(x)    : プライオリティキューにxを追加
    erase(x)   : プライオリティーキューからxを(疑似的に)削除
    clean()    : 削除予定でトップに来た要素をq,pからpop
    pop((exc)) : トップの要素をqからpop (qが空の場合、excを返す)
    top((exc)) : トップの要素の値を取得  (qが空の場合、excを返す)
    '''
    def __init__(self):
        self.q = []
        self.p = []
    def build(self, a):
        self.q = a
        heapify(self.q)
    def push(self, x):
        heappush(self.q, x)
    def erase(self, x):
        heappush(self.p, x)
        self.clean()
    def clean(self):
        while self.p and self.q and self.q[0]==self.p[0]:
          heappop(self.q)
          heappop(self.p)
    def pop(self, exc=None):
        self.clean()
        if self.q:
          return heappop(self.q)
        return exc
    def top(self, exc=None):
        self.clean()
        if self.q:
          return self.q[0]
        return exc


def main():
    N = NI()
    T = []

    hq1 = Heapq()
    hq2 = Heapq()
    T1 = [0] * N
    T2 = [0] * N

    for i in range(N):
        k, *t = NMI()
        t = deque(t)
        if len(t) > 0:
            x = t.popleft() * (-1)
            hq1.push((x, i))
            T1[i] = x
        if len(t) > 0:
            x = t.popleft() * (-1)
            hq2.push((x, i))
            T2[i] = x
        T.append(t)

    M = NI()
    A = NLI()

    # print(hq1.q)
    # print(hq2.q)

    for a in A:
        if a == 1:
            x, i = hq1.pop(exc=(0, 0))
            t = T2[i]
            hq2.erase((t, i))
            hq1.push((t, i))
            T1[i] = T2[i]
            if len(T[i]) > 0:
                t = T[i].popleft()
                T2[i] = t * (-1)
                hq2.push((t * (-1), i))
            else:
                T2[i] = 0
            print(-x)


        else:
            x1, i1 = hq1.pop(exc=(0, 0))
            x2, i2 = hq2.pop(exc=(0, 0))

            if x1 < x2:
                # x1を採用
                x, i = x1, i1
                hq2.push((x2, i2))
                t = T2[i]
                hq2.erase((t, i))
                hq1.push((t, i))
                T1[i] = T2[i]
                if len(T[i]) > 0:
                    t = T[i].popleft()
                    T2[i] = t * (-1)
                    hq2.push((t * (-1), i))
                else:
                    T2[i] = 0
                print(-x)

            else:
                x, i = x2, i2
                hq1.push((x1, i1))

                if len(T[i]) > 0:
                    t = T[i].popleft()
                    # print(x, i, -t)
                    T2[i] = t * (-1)
                    hq2.push((t*(-1), i))
                else:
                    T2[i] = 0
                print(-x)

        # print(T1)
        # print(T2)
        # print(hq1.q)
        # print(hq2.q)


if __name__ == "__main__":
    main()
