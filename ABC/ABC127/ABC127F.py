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


# 削除可能heapq
from heapq import *
class Heapq:
    '''
    最大値を取りたいときはmaxheap=Trueにする

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


class SlopeTrick:
    def __init__(self):
        """
        区分線形凸関数 f を、傾きの変化点の多重集合に置き換えて管理することで、特定の関数操作が簡潔に行えるようにするもの
        https://maspypy.com/slope-trick-1-%e8%a7%a3%e8%aa%ac%e7%b7%a8

        L: 傾きが0以下の部分について、傾きの変化点全体の多重集合
        R: 傾きが0以上の部分について、傾きの変化点全体の多重集合
        隣り合う2点間での傾きが等しい（とくにL[0]とR[0]の間はfの最小値をとる）
        """
        self.L = Heapq(maxheap=True)
        self.R = Heapq()
        self.INF = 1<<60
        self.L.push(-self.INF)
        self.R.push(self.INF)
        self.minf = 0
        self.argmin = None

    def add(self, a, b):
        """|x-a|+bを加算"""
        # 右側加算 max(0, x-a)
        self.minf += max(0, self.L.top() - a)
        self.L.push(a)
        self.R.push(self.L.pop())

        # 左側加算 max(0, a-x)
        self.minf += max(0, a - self.R.top())
        self.R.push(a)
        self.L.push(self.R.pop())

        self.minf += b
        # fの最小値をとるxのうち最小のもの
        self.argmin = self.L.top()


def main():
    Q = NI()
    S = SlopeTrick()
    for _ in range(Q):
        q, *X = NMI()
        if q == 1:
            S.add(*X)
        else:
            print(S.argmin, S.minf)


if __name__ == "__main__":
    main()
