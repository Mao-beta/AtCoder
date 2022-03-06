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
    a, N = NMI()
    seen = set()

    hq = []
    heapify(hq)
    heappush(hq, [0, 1])

    while hq:
        k, x = heappop(hq)

        if x == N:
            print(k)
            exit()

        if x in seen:
            continue

        seen.add(x)
        ax = a * x
        if len(str(ax)) <= len(str(N)):
            heappush(hq, [k+1, ax])

        x_str = str(x)
        for i in range(1, len(x_str)):
            goto = x_str[-i:] + x_str[:-i]
            if goto[0] == "0": break

            heappush(hq, [k+i, int(goto)])

    print(-1)


if __name__ == "__main__":
    main()
