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


class PrioritySumStructure:
    """
    昇順で先頭k個の和を保持するデータ構造(kは固定)
    query O(1)
    insert, erase ならしO(logN)

    最大値を得るheapKに下位K個をいれ、
    最小値を得るheapElseに残りを入れる
    全体でK個以上あるときはheapKの要素をK個に保つ
    """
    def __init__(self, k):
        assert k > 0

        self.k = k
        self.size = 0
        self.ksum = 0
        self.heapK = Heapq(maxheap=True)
        self.heapElse = Heapq()

    def add(self, x):
        if self.size < self.k:
            self.heapK.push(x)
            self.ksum += x
        else:
            kth = self.heapK.top()
            if kth <= x:
                self.heapElse.push(x)
            else:
                self.heapK.push(x)
                self.ksum += x

        self.size += 1
        self.adjust()

    def erase(self, x):
        assert self.size > 0

        if self.size <= self.k:
            self.heapK.erase(x)
            self.ksum -= x
        else:
            kth = self.heapK.top()
            if kth < x:
                self.heapElse.erase(x)
            else:
                self.heapK.erase(x)
                self.ksum -= x

        self.size -= 1
        self.adjust()

    def adjust(self):
        while self.heapElse.size > 0 and self.heapK.size < self.k:
            x = self.heapElse.pop()
            self.heapK.push(x)
            self.ksum += x

        while self.heapK.size > self.k:
            x = self.heapK.pop()
            self.heapElse.push(x)
            self.ksum -= x

    def query(self):
        return self.ksum

    def debug(self):
        print(self.heapK.debug(), self.heapElse.debug())


def main(N, M, K, A):
    D = PrioritySumStructure(K)
    for i in range(M):
        D.add(A[i])

    ans = [D.query()]
    for i in range(M, N):
        D.add(A[i])
        D.erase(A[i-M])
        ans.append(D.query())

    return ans


def guchoku(N, M, K, A):
    ans = []
    for i in range(N-M+1):
        X = sorted(A[i:i+M])
        ans.append(sum(X[:K]))
    return ans


if __name__ == "__main__":
    N, M, K = NMI()
    A = NLI()
    ans = main(N, M, K, A)
    print(*ans)
    exit()

    import random
    N = 10
    for i in range(100):
        M = random.randint(1, N)
        K = random.randint(1, M)
        A = [random.randint(1, 10) for _ in range(N)]

        # print("#", N, M, K)
        # print("#", A)
        ans = main(N, M, K, A)
        # print(*ans)
        ans2 = guchoku(N, M, K, A)
        # print(*ans)
        assert ans == ans2