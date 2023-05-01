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
    A = NLI()
    D = defaultdict(list)
    ans = 0
    for l in range(1, N+1):
        ans += l // 2 * (N-l+1)

    for i, a in enumerate(A):
        D[a].append(min(i+1, N-i))

    for x in range(1, N+1):
        D[x].sort()
        n = len(D[x])
        for i in range(n):
            d = D[x][i]
            # print((n-i-1) * d)
            ans -= (n-i-1) * d

    print(ans)


if __name__ == "__main__":
    main()
