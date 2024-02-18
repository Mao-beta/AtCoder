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
    X = SI()
    cum = [0]
    for s in X:
        cum.append(cum[-1] + int(s))
    ans = []
    up = 0
    for c in cum[1:][::-1]:
        c += up
        t, r = divmod(c, 10)
        ans.append(str(r))
        up = t

    if up > 0:
        ans.append(str(up)[::-1])

    print("".join(ans)[::-1])


if __name__ == "__main__":
    main()
