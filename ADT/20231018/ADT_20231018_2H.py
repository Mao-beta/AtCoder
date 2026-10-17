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


def main():
    N = NI()
    XY = EI(N)

    class Frac:
        def __init__(self, bo, si):
            self.si = si
            self.bo = bo

        def __lt__(self, other):
            return self.si * other.bo < self.bo * other.si

        def __eq__(self, other):
            return self.si * other.bo == self.bo * other.si

        def __repr__(self):
            return f"{self.si}/{self.bo}"

    L = [[Frac(x, y-1), Frac(x-1, y)] for x, y in XY]
    L.sort(key=lambda x: x[1])

    now = Frac(1, 0)
    ans = 0
    for l, r in L:
        if now > l:
            continue
        ans += 1
        now = r
    print(ans)


if __name__ == "__main__":
    main()
