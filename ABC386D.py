import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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
    N, M = NMI()
    X2YC = defaultdict(list)
    for _ in range(M):
        x, y, c = SMI()
        x, y = int(x)-1, int(y)-1
        X2YC[x].append([y, c])
    r = N
    for x in sorted(X2YC.keys()):
        X2YC[x].sort()
        t = "B"
        for y, c in X2YC[x]:
            if t == "W" and c == "B":
                print("No")
                return
            if c == "B" and r <= y:
                print("No")
                return
            t = c
            if c == "W":
                r = min(r, y)
    print("Yes")


if __name__ == "__main__":
    main()
