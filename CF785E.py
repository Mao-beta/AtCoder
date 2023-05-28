import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

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


def main_MS():
    N, Q = NMI()
    querys = EI(Q)
    ans = 0
    A = list(range(1, N+1))
    sz = 3000 # 1500や5000ではTLE
    bnum = (N+sz-1) // sz
    buckets = [SortedMultiset(A[i*sz: (i+1)*sz]) for i in range(bnum)]

    for l, r in querys:
        l, r = l-1, r-1
        if l > r:
            l, r = r, l
        al, ar = A[l], A[r]
        bl, br = l//sz, r//sz
        # print(l, r, al, ar, bl, br, (l+sz-1)//sz*sz)

        if bl == br:
            for idx in range(l+1, r):
                a = A[idx]
                if a > al:
                    ans += 1
                elif a < al:
                    ans -= 1

                if a > ar:
                    ans -= 1
                elif a < ar:
                    ans += 1

        else:
            for idx in range(l+1, (l//sz + 1)*sz):
                # print("lidx", idx)
                a = A[idx]
                if a > al:
                    ans += 1
                elif a < al:
                    ans -= 1

                if a > ar:
                    ans -= 1
                elif a < ar:
                    ans += 1

            for b in range(bl+1, br):
                # print(b)
                ms = buckets[b]
                # alより大きいものを足す
                ans += len(ms) - ms.index_right(al)
                # alより小さいものを引く
                ans -= ms.index(al)
                # arより小さいものを足す
                ans += ms.index(ar)
                # arより大きいものを引く
                ans -= len(ms) - ms.index_right(ar)

            for idx in range(r//sz*sz, r):
                # print("ridx", idx)
                a = A[idx]
                if a > al:
                    ans += 1
                elif a < al:
                    ans -= 1

                if a > ar:
                    ans -= 1
                elif a < ar:
                    ans += 1

        if al > ar:
            ans -= 1
        elif al < ar:
            ans += 1

        A[l], A[r] = A[r], A[l]
        buckets[bl].discard(al)
        buckets[bl].add(ar)
        buckets[br].discard(ar)
        buckets[br].add(al)
        # print(A)
        # print(buckets)
        print(ans)


def main():
    N, Q = NMI()
    querys = EI(Q)
    ans = 0
    A = list(range(1, N+1))
    sz = 3000 # 1000,5000ではTLE 1500,3000ではAC
    bnum = (N+sz-1) // sz
    buckets = [sorted(A[i*sz: (i+1)*sz]) for i in range(bnum)]

    for l, r in querys:
        l, r = l-1, r-1
        if l > r:
            l, r = r, l
        al, ar = A[l], A[r]
        bl, br = l//sz, r//sz
        # print(l, r, al, ar, bl, br, (l+sz-1)//sz*sz)

        if bl == br:
            for idx in range(l+1, r):
                a = A[idx]
                if a > al:
                    ans += 1
                elif a < al:
                    ans -= 1

                if a > ar:
                    ans -= 1
                elif a < ar:
                    ans += 1

        else:
            for idx in range(l+1, (l//sz + 1)*sz):
                # print("lidx", idx)
                a = A[idx]
                if a > al:
                    ans += 1
                elif a < al:
                    ans -= 1

                if a > ar:
                    ans -= 1
                elif a < ar:
                    ans += 1

            for b in range(bl+1, br):
                # print(b)
                ms = buckets[b]
                # alより大きいものを足す
                ans += len(ms) - bisect.bisect_right(ms, al)
                # alより小さいものを引く
                ans -= bisect.bisect_left(ms, al)
                # arより小さいものを足す
                ans += bisect.bisect_left(ms, ar)
                # arより大きいものを引く
                ans -= len(ms) - bisect.bisect_right(ms, ar)

            for idx in range(r//sz*sz, r):
                # print("ridx", idx)
                a = A[idx]
                if a > al:
                    ans += 1
                elif a < al:
                    ans -= 1

                if a > ar:
                    ans -= 1
                elif a < ar:
                    ans += 1

        if al > ar:
            ans -= 1
        elif al < ar:
            ans += 1

        A[l], A[r] = A[r], A[l]
        buckets[bl].remove(al)
        buckets[bl].append(ar)
        buckets[bl].sort()
        buckets[br].remove(ar)
        buckets[br].append(al)
        buckets[br].sort()
        # print(A)
        # print(buckets)
        print(ans)


if __name__ == "__main__":
    main()
