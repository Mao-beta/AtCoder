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
    N, M, D = NMI()
    A = NLI()
    B = NLI()
    B.sort()
    ans = -1
    for a in A:
        idx = bisect.bisect_right(B, a+D)
        if idx == 0:
            continue
        b = B[idx-1]
        if abs(a-b) > D:
            continue
        ans = max(ans, a+b)
    print(ans)


if __name__ == "__main__":
    main()
