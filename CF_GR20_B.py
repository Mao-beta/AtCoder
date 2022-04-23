import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

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
    for _ in range(N):
        S = SI()
        now = 0
        ans = "YES"
        for s in S:
            if s == "A":
                now += 1
            else:
                now -= 1
            if now < 0:
                ans = "NO"

        if S[-1] != "B":
            ans = "NO"

        print(ans)



if __name__ == "__main__":
    main()
