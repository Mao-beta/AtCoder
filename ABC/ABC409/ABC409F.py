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

    
def main():
    N, Q = NMI()
    XY = EI(N)
    MS = SortedMultiset()
    Ls = defaultdict(set)

    def f(i, j):
        return i * 10000 + j

    def g(ij):
        return divmod(ij, 10000)

    class UnionFind:
        def __init__(self, n):
            # 親要素のノード番号を格納　xが根のとき-(サイズ)を格納
            self.par = [-1 for i in range(n)]
            self.n = n
            self.roots = set(range(n))
            self.group_num = n
            self.members = [set() for _ in range(n)]

            for i in range(n):
                self.members[i].add(i)

        def find(self, x):
            # 根ならその番号を返す
            if self.par[x] < 0:
                return x
            else:
                # 親の親は親
                self.par[x] = self.find(self.par[x])
                return self.par[x]

        def is_same(self, x, y):
            # 根が同じならTrue
            return self.find(x) == self.find(y)

        def unite(self, x, y):
            x = self.find(x)
            y = self.find(y)
            if x == y: return

            # 木のサイズを比較し、小さいほうから大きいほうへつなぐ
            if self.par[x] > self.par[y]:
                x, y = y, x

            # print(f"{self.members[x]=} {self.members[y]=} {x=} {y=}")
            for mx in self.members[x]:
                for my in self.members[y]:
                    mx2, my2 = mx, my
                    if mx2 > my2:
                        mx2, my2 = my2, mx2
                    d = abs(XY[mx2][0] - XY[my2][0]) + abs(XY[mx2][1] - XY[my2][1])
                    # print(f"deleted {mx2=} {my2=} {d=}")
                    Ls[d].discard(f(mx2, my2))
                    if len(Ls[d]) == 0:
                        MS.discard(d)

            self.group_num -= 1
            self.roots.discard(y)
            assert self.group_num == len(self.roots)

            self.members[x] |= self.members[y]
            self.members[y] = set()

            self.par[x] += self.par[y]
            self.par[y] = x

        def size(self, x):
            return -self.par[self.find(x)]

        def get_members(self, x):
            root = self.find(x)
            return self.members[root]

        def get_roots(self):
            return self.roots

        def group_count(self):
            return len(self.roots)

        def all_group_members(self):
            return self.members

        def __repr__(self):
            return '\n'.join('{}: {}'.format(r, self.members[r]) for r in self.roots)


    uf = UnionFind(N + Q)

    for i, (x, y) in enumerate(XY):
        for j, (x2, y2) in enumerate(XY):
            d = abs(x-x2) + abs(y-y2)
            if i < j and d not in MS:
                MS.add(d)
                Ls[d].add(f(i, j))
                
    for _ in range(Q):
        q, *X = NMI()
        print()
        print(f"{q=} {X=}")
        print(MS)
        print(Ls)
        print(uf)
        if q == 1:
            a, b = X
            td = 10**18
            ti = [0]

            for i, (x, y) in enumerate(XY):
                d = abs(a-x) + abs(b-y)
                if d < td:
                    td = d
                    ti = [i]
                elif d == td:
                    ti.append(i)
            for i in ti:
                Ls[td].add(f(i, len(XY)))
            if td not in MS:
                MS.add(td)
            XY.append([a, b])
        elif q == 2:
            if len(MS) == 0:
                print(-1)
            else:
                mind = MS[0]
                for ij in list(Ls[mind]):
                    i, j = g(ij)
                    uf.unite(i, j)
                Ls[mind] = set()
                MS.discard(mind)
                print(mind)
        else:
            u, v = X
            u, v = u-1, v-1
            if uf.is_same(u, v):
                print("Yes")
            else:
                print("No")


if __name__ == "__main__":
    main()
