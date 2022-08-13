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
    N, M = NMI()

    def rec(now):
        if len(ans) == N:
            print(*ans)
            return

        for goto in range(now+1, M+1):
            ans.append(goto)
            rec(goto)
            ans.pop()

    for i in range(1, M+1):
        ans = [i]
        rec(i)


if __name__ == "__main__":
    main()
