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
    AB = EI(N)
    ans = 1
    ca, cb = AB[0]
    for i, (a, b) in enumerate(AB, start=1):
        if i == 1:
            continue
        if (a + cb - 1) // cb > (ca + b - 1) // b:
            ans = i
            ca, cb = a, b

    for i, (a, b) in enumerate(AB, start=1):
        if i == ans:
            continue
        if (a + cb - 1) // cb >= (ca + b - 1) // b:
            print(-1)
            exit()

    print(ans)


if __name__ == "__main__":
    main()
