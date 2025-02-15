import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product


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
    A = [SLI() for _ in range(N)]
    A = [S for S in zip(*A)]
    ans = []
    for i, a in enumerate(A, start=1):
        C = Counter(a)
        if C["nyanpass"] == N-1:
            ans.append(i)
    if len(ans) == 1:
        print(ans[0])
    else:
        print(-1)


if __name__ == "__main__":
    main()
