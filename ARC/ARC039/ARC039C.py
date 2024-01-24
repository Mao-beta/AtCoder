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



# https://github.com/tatyam-prime/SortedSet/blob/main/SortedSet.py
# https://github.com/tatyam-prime/SortedSet/blob/main/SortedMultiset.py
import math
from bisect import bisect_left, bisect_right, insort
from typing import Generic, Iterable, Iterator, TypeVar, Union, List

T = TypeVar('T')


class SortedSet(Generic[T]):
    BUCKET_RATIO = 50
    REBUILD_RATIO = 170

    def _build(self, a=None) -> None:
        "Evenly divide `a` into buckets."
        if a is None: a = list(self)
        size = self.size = len(a)
        bucket_size = int(math.ceil(math.sqrt(size / self.BUCKET_RATIO)))
        self.a = [a[size * i // bucket_size: size * (i + 1) // bucket_size] for i in range(bucket_size)]

    def __init__(self, a: Iterable[T] = []) -> None:
        "Make a new SortedSet from iterable. / O(N) if sorted and unique / O(N log N)"
        a = list(a)
        if not all(a[i] < a[i + 1] for i in range(len(a) - 1)):
            a = sorted(set(a))
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
        return "SortedSet" + str(self.a)

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

    def add(self, x: T) -> bool:
        "Add an element and return True if added. / O(√N)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return True
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        if i != len(a) and a[i] == x: return False
        a.insert(i, x)
        self.size += 1
        if len(a) > len(self.a) * self.REBUILD_RATIO:
            self._build()
        return True

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


class Segments:
    INF = 10**10
    def __init__(self):
        """
        未到達の半開区間[l, r)を管理する。
        """
        self.L = None
        self.R = None

    def _build(self):
        self.L = SortedSet()
        self.R = SortedSet()
        self.L.add(-self.INF)
        self.R.add(self.INF)

    def insert(self, x):
        """
        xを到達済みにする。xを含む区間があれば分割する
        """
        if self.L is None:
            self._build()

        # idx = self.L.bisect_right(x)
        idx = self.L.index_right(x)
        l = self.L[idx-1]
        r = self.R[idx-1]
        if l <= x < r:
            self.L.discard(l)
            self.R.discard(r)
            l1, r1 = l, x
            l2, r2 = x+1, r
            if l < x:
                self.L.add(l1)
                self.R.add(r1)
            if x+1 < r:
                self.L.add(l2)
                self.R.add(r2)

    def search_upper(self, x):
        """
        現在地xから一番近い上側の未到達座標を得る。xは到達済みの前提
        """
        # idx = self.L.bisect_left(x)
        # return self.L[idx]
        return self.L.gt(x)


    def search_lower(self, x):
        """
        現在地xから一番近い下側の未到達座標を得る。xは到達済みの前提
        """
        # idx = self.R.bisect_right(x)
        # return self.R[idx-1]-1
        return self.R.le(x) - 1


def main():
    K = NI()
    S = SI()
    M = 200001
    X = [Segments() for _ in range(2 * M)]
    Y = [Segments() for _ in range(2 * M)]
    X[0].insert(0)
    Y[0].insert(0)

    D = {s: i for i, s in enumerate("LRUD")}
    DX = [-1, 1, 0, 0]
    DY = [0, 0, 1, -1]

    x, y = 0, 0
    for s in S:
        d = D[s]
        dx, dy = DX[d], DY[d]
        if dx == 0: # y方向
            nx = x
            if dy > 0:
                ny = X[x].search_upper(y)
            else:
                ny = X[x].search_lower(y)
        else:
            ny = y
            if dx > 0:
                nx = Y[y].search_upper(x)
            else:
                nx = Y[y].search_lower(x)
        X[nx].insert(ny)
        Y[ny].insert(nx)
        x, y = nx, ny

    print(x, y)



if __name__ == "__main__":
    main()
