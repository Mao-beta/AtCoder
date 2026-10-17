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


def main():
    N = NI()
    AB = [NLI() for _ in range(N)]
    ans = 0
    for a, b in AB:
        r = b - a
        if r % 100 >= 50:
            ans += 1
        if r % 10 >= 5:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
