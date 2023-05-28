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

import sys
from typing import List, Tuple
from heapq import heapify, heappop

INT_MAX = 10 ** 15
INT_MIN = -10 ** 15


class kDTree:
    def __init__(self, points: List[List[int, int]], divx=True):
        self.l = None
        self.r = None
        self.xmin = INT_MAX
        self.xmax = INT_MIN
        self.ymin = INT_MAX
        self.ymax = INT_MIN
        self.size = 0

        for p in points:
            x, y = p
            self.xmin = min(self.xmin, x)
            self.xmax = max(self.xmax, x)
            self.ymin = min(self.ymin, y)
            self.ymax = max(self.ymax, y)

        self.size = len(points)

        if self.size <= 1:
            return

        cen = self.size // 2
        if divx:
            points.sort(key=lambda x: x[0])
        else:
            points.sort(key=lambda x: x[1])

        self.l = kDTree(points[:cen], not divx)
        self.r = kDTree(points[cen:], not divx)

    def count(self, x1, x2, y1, y2):
        stack = [self]
        count = 0
        while stack:
            node = stack.pop()
            if node is None:
                continue

            if x2 < node.xmin or node.xmax < x1 or y2 < node.ymin or node.ymax < y1:
                continue

            if x1 <= node.xmin and node.xmax <= x2 and y1 <= node.ymin and node.ymax <= y2:
                count += node.size
            else:
                stack.append(node.l)
                stack.append(node.r)

        return count


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


def _main():
    N = NI()

    points = [NLI() for _ in range(N)]

    kdtree = kDTree(points)
    Q = NI()
    for i in range(Q):
        sx, tx, sy, ty = NMI()
        ans = kdtree.find_points(sx, tx, sy, ty)
        ans.sort()
        if ans:
            print(*ans, sep="\n")
        print()


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
