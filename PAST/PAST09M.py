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


from sortedcontainers import SortedList

def main():
    N, Q = NMI()
    S = SLI()
    L = SortedList()
    for i, s in enumerate(S):
        L.add((s, i))
    for _ in range(Q):
        x, t = SMI()
        x = int(x)-1
        s, i = L[x]
        L.discard((s, i))
        L.add((t, i))
    
    ans = ["" for _ in range(N)]
    for s, i in L:
        ans[i] = s
    print(*ans, sep=" ")


if __name__ == "__main__":
    main()
