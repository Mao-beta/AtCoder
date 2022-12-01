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


def main():
    X, Y = NMI()
    ans = [[X, Y]]
    while X > 1 or Y > 1:
        if X >= Y:
            X -= Y
        else:
            Y -= X
        ans.append([X, Y])

    print(len(ans) - 1)
    for x, y in ans[::-1][1:]:
        print(x, y)


if __name__ == "__main__":
    main()
