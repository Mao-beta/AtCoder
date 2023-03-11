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
    A = [x-1 for x in A]
    seen = [0] * N
    for i in range(N):
        if seen[i] == 0:
            seen[A[i]] = 1

    ans = [i+1 for i, x in enumerate(seen) if x == 0]
    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    main()
