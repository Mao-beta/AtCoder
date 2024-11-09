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


def adjlist(n, edges, directed=False, in_origin=1) -> list[list[int]]:
    if len(edges) == 0:
        return [[] for _ in range(n)]

    weighted = True if len(edges[0]) > 2 else False
    if in_origin == 1:
        if weighted:
            edges = [[x-1, y-1, w] for x, y, w in edges]
        else:
            edges = [[x-1, y-1] for x, y in edges]

    res = [[] for _ in range(n)]

    if weighted:
        for u, v, c in edges:
            res[u].append([v, c])
            if not directed:
                res[v].append([u, c])

    else:
        for u, v in edges:
            res[u].append(v)
            if not directed:
                res[v].append(u)

    return res


# https://github.com/tatyam-prime/SortedSet/blob/main/SortedSet.py
# https://github.com/tatyam-prime/SortedSet/blob/main/SortedMultiset.py
import math
from bisect import bisect_left, bisect_right, insort
from typing import Generic, Iterable, Iterator, TypeVar, Union, List

T = TypeVar('T')

class SortedMultiset(Generic[T]):
    BUCKET_RATIO = 50
    REBUILD_RATIO = 170

    def _build(self, a=None) -> None:
        "Evenly divide `a` into buckets."
        if a is None: a = list(self)
        size = self.size = len(a)
        bucket_size = int(math.ceil(math.sqrt(size / self.BUCKET_RATIO)))
        self.a = [a[size * i // bucket_size: size * (i + 1) // bucket_size] for i in range(bucket_size)]

    def __init__(self, a: Iterable[T] = []) -> None:
        "Make a new SortedMultiset from iterable. / O(N) if sorted / O(N log N)"
        a = list(a)
        if not all(a[i] <= a[i + 1] for i in range(len(a) - 1)):
            a = sorted(a)
        self._build(a)

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i: yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i): yield j

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return "SortedMultiset" + str(self.a)

    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1: len(s) - 1] + "}"

    def _find_bucket(self, x: T) -> List[T]:
        "Find the bucket which should contain x. self must not be empty."
        for a in self.a:
            if x <= a[-1]: return a
        return a

    def __contains__(self, x: T) -> bool:
        if self.size == 0: return False
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        return i != len(a) and a[i] == x

    def count(self, x: T) -> int:
        "Count the number of x."
        return self.index_right(x) - self.index(x)

    def add(self, x: T) -> None:
        "Add an element. / O(√N)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return
        a = self._find_bucket(x)
        insort(a, x)
        self.size += 1
        if len(a) > len(self.a) * self.REBUILD_RATIO:
            self._build()

    def discard(self, x: T) -> bool:
        "Remove an element and return True if removed. / O(√N)"
        if self.size == 0: return False
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        if i == len(a) or a[i] != x: return False
        a.pop(i)
        self.size -= 1
        if len(a) == 0: self._build()
        return True

    def lt(self, x: T) -> Union[T, None]:
        "Find the largest element < x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] < x:
                return a[bisect_left(a, x) - 1]

    def le(self, x: T) -> Union[T, None]:
        "Find the largest element <= x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] <= x:
                return a[bisect_right(a, x) - 1]

    def gt(self, x: T) -> Union[T, None]:
        "Find the smallest element > x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] > x:
                return a[bisect_right(a, x)]

    def ge(self, x: T) -> Union[T, None]:
        "Find the smallest element >= x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] >= x:
                return a[bisect_left(a, x)]

    def __getitem__(self, x: int) -> T:
        "Return the x-th element, or IndexError if it doesn't exist."
        if x < 0: x += self.size
        if x < 0: raise IndexError
        for a in self.a:
            if x < len(a): return a[x]
            x -= len(a)
        raise IndexError

    def index(self, x: T) -> int:
        "Count the number of elements < x."
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def index_right(self, x: T) -> int:
        "Count the number of elements <= x."
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans


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
    UV = EI(M)
    G = adjlist(N, UV)
    C = [0] * N
    INF = 10**18
    for i in range(N):
        for v in G[i]:
            C[i] += A[v]
        C[i] *= INF
        C[i] += i
    ans = 0
    MS = SortedMultiset(C[:])
    seen = [0] * N
    while len(MS) > 0:
        x = MS[0]
        # print(x, MS)
        cost, idx = divmod(x, INF)
        ans = max(ans, cost)
        # print(cost)
        MS.discard(x)
        seen[idx] = 1
        for v in G[idx]:
            if seen[v]:
                continue
            # print(N, v, CC)
            MS.discard(C[v])
            C[v] -= A[idx] * INF
            if C[v] // INF > 0:
                MS.add(C[v])

    print(ans)


if __name__ == "__main__":
    main()
