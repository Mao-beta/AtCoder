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


def main():
    N = NI()
    S = [SI() for _ in range(N)]

    def dfs(now):
        win = False
        sn = S[now]
        used.add(now)

        if len(used) % 2:
            for nex in range(N):
                if nex in used:
                    continue
                if S[nex][0] == sn[-1]:
                    res = dfs(nex)
                    if not res:
                        win = True

            used.discard(sn)
            return win

        else:
            win = True
            for nex in range(N):
                if nex in used:
                    continue
                if S[nex][0] == sn[-1]:
                    res = dfs(nex)
                    if res:
                        win = False

            used.discard(sn)
            return win

    for s in range(N):
        used = set()
        res = dfs(s)
        if res:
            print("First")
            return
    print("Second")


if __name__ == "__main__":
    main()
