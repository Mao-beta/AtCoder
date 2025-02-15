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
    N = NI()
    P = [math.log10(i/10) if i >= 10 else 0 for i in range(101)]

    for _ in range(N):
        A, B = NMI()
        x = B * math.log10(A)
        Z = math.floor(x)
        XY = x - Z
        idx = bisect.bisect_left(P, XY)-1
        if idx == -1:
            idx = 10
        print(idx//10, idx%10, Z)



if __name__ == "__main__":
    main()
