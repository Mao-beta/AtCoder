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
    ST = [SLI() for _ in range(N)]
    ans = []
    for i in range(10000):
        i = str(i).zfill(4)
        ok = True
        for s, t in ST:
            tmp = 5
            for ii, si in zip(i, s):
                if ii == si:
                    tmp -= 1
            tmp = min(tmp, 3)
            if tmp != int(t):
                ok = False
                break
        if ok:
            ans.append(i)

    if len(ans) > 1:
        print("Can't Solve")
    else:
        print(ans[0])


if __name__ == "__main__":
    main()
