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
    N = NI()
    S = [SI() for _ in range(N)]
    E = []
    for s in S:
        start, end = map(int, s.split("-"))
        start = start - start % 5
        end = (end + 4) // 5 * 5
        if end % 100 >= 60:
            end = end // 100 * 100 + 100 + end % 100 - 60
        E.append([start, -1])
        E.append([end, 1])
    E.sort()

    state = 0
    for t, s in E:
        new = state + s

        if state == 0 and new < 0:
            print(str(t).zfill(4), end="-")
        elif state < 0 and new == 0:
            print(str(t).zfill(4))
        state = new


if __name__ == "__main__":
    main()
