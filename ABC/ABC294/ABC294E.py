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
    L, N, M = NMI()
    VL1 = deque(EI(N))
    VL2 = deque(EI(M))
    i = 0
    j = 0
    p = -1
    q = -1
    ans = 0
    while VL1 or VL2:
        if i <= j:
            v, l = VL1.popleft()
            if q == v:
                ans += min(j-i, l)
            i += l
            p = v
        else:
            v, l = VL2.popleft()
            if p == v:
                ans += min(i-j, l)
            j += l
            q = v
    print(ans)


if __name__ == "__main__":
    main()
