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
    ABC = [NLI() for _ in range(M)]
    ABC = [{a-1, b-1, c-1} for a, b, c in ABC]

    def check(case, abc):
        safe = set()
        for x in abc:
            if (case >> x) & 1 == 0:
                safe.add(x)

        return safe


    ans = 0
    for case in range(1, 1<<N):

        ok = True
        X = set()
        for abc in ABC:
            safe = check(case, abc)
            if len(safe) == 0:
                ok = False
                break
            elif len(safe) == 1:
                X |= safe

        if not ok: continue

        ans = max(ans, len(X))
        # print(bin(case)[2:].zfill(N), ans, len(X), X)

    print(ans)


if __name__ == "__main__":
    main()
