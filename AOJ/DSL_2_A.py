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


from atcoder.segtree import SegTree

def main():
    N, Q = NMI()
    tree = SegTree(min, (1<<31)-1, [(1<<31)-1]*N)
    for _ in range(Q):
        c, x, y = NMI()
        if c == 0:
            tree.set(x, y)
        else:
            print(tree.prod(x, y+1))


if __name__ == "__main__":
    main()
