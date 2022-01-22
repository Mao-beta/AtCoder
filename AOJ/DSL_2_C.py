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


from bisect import bisect_left, bisect_right
from typing import List, Optional, Tuple
class KDTree(object):
    def __init__(self, n: int) -> None:
        self.n = n
        self.root = int(math.sqrt(n))
        self.coordinates = [(0, 0, 0)] * n
        self.low: List[int] = []
        self.high: List[int] = []
        self.coordinates_: List[Tuple[List[int], List[Tuple[int, int, int]]]] = []

    def add(self, x: int, y: int, idx: int) -> None:
        self.coordinates[idx] = (x, y, idx)

    def prepare(self) -> None:
        self.coordinates.sort()
        self.low = [x for x, _, _ in self.coordinates[::self.root]]
        self.high = [x for x, _, _
                     in self.coordinates[self.root - 1::self.root]] + [sys.maxsize]
        tmp = [sorted(self.coordinates[i: i + self.root], key=lambda x: x[1])
               for i in range(0, self.n, self.root)]
        self.coordinates_ = [([y for _, y, _ in xyi], xyi) for xyi in tmp]

    def find_points(self, sx: int, tx: int, sy: int, ty: int) -> Optional[List[int]]:
        ans = []
        for i in range(bisect_left(self.high, sx), bisect_right(self.low, tx)):
            k, v = self.coordinates_[i]
            for j in range(bisect_left(k, sy), bisect_right(k, ty)):
                if sx <= v[j][0] <= tx:
                    ans.append(v[j][2])
        return ans


def main():
    N = NI()

    kdtree = KDTree(N)

    for i in range(N):
        x, y = NMI()
        kdtree.add(x, y, i)

    kdtree.prepare()
    Q = NI()
    for i in range(Q):
        sx, tx, sy, ty = NMI()
        ans = kdtree.find_points(sx, tx, sy, ty)
        ans.sort()
        if ans:
            print(*ans, sep="\n")
        print()


if __name__ == "__main__":
    main()
