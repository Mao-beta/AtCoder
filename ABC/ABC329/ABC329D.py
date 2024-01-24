import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product
from sortedcontainers import SortedDict

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


# 削除可能heapq
from heapq import *
class Heapq:
    '''
    最大値を取りたいときはasc=Trueにする

    Heapq()    : 本体qと削除用pの2本のheapqを用意する
    build(a)   : 配列aからプライオリティキューqを構築する
    push(x)    : プライオリティキューにxを追加
    erase(x)   : プライオリティーキューからxを(疑似的に)削除
    clean()    : 削除予定でトップに来た要素をq,pからpop
    pop((exc)) : トップの要素をqからpop (qが空の場合、excを返す)
    top((exc)) : トップの要素の値を取得  (qが空の場合、excを返す)
    size       : 有効な値の数を取得
    debug()    : 現在のheapの中身（削除処理すみ）を取得
    '''
    def __init__(self, maxheap=False):
        self.q = []
        self.p = []
        self.size = 0
        self.maxheap = maxheap

    def build(self, a):
        self.q = a
        heapify(self.q)
        self.size = len(a)

    def push(self, x):
        if self.maxheap: x *= -1
        heappush(self.q, x)
        self.size += 1

    def erase(self, x):
        if self.maxheap: x *= -1
        heappush(self.p, x)
        self.clean()
        self.size -= 1

    def clean(self):
        while self.p and self.q and self.q[0]==self.p[0]:
            heappop(self.q)
            heappop(self.p)

    def pop(self, exc=None):
        self.clean()
        if self.q:
            self.size -= 1
            res = heappop(self.q)
            if self.maxheap: res *= -1
            return res
        return exc

    def top(self, exc=None):
        self.clean()
        if self.q:
            res = self.q[0]
            if self.maxheap: res *= -1
            return res
        return exc

    def debug(self):
        p = self.p.copy()
        q = self.q.copy()
        d = []
        while q:
            x = heappop(q)
            if p and p[0] == x:
                heappop(p)
                continue
            else:
                if self.maxheap: x *= -1
                d.append(x)
        return d


def main():
    N, M = NMI()
    A = NLI()
    D = [Heapq() for _ in range(M+1)]
    D[0].build(list(range(1, N+1)))
    X = [0] * (N+1)
    top = 0
    for a in A:
        k = X[a]
        X[a] += 1
        D[k].erase(a)
        D[k+1].push(a)
        top = max(top, k+1)
        print(D[top].top())


if __name__ == "__main__":
    main()
