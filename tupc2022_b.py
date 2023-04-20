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
    N, M, K = NMI()
    AB = EI(M) + [[N+1, 0]]
    now = 0
    ans = 0
    for i in range(M):
        a, b = AB[i]
        na, nb = AB[i+1]
        now += b
        ans += max(min(na-a, now-K), 0)
        now -= na - a
        now = max(now, 0)
    print(ans)


if __name__ == "__main__":
    main()
