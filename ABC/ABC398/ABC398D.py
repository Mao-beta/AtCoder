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
    N, R, C = NMI()
    S = SI()
    INF = 10**8
    ans = [0] * N
    D = {0}
    X, Y = 0, 0
    for i, s in enumerate(S):
        if s == "N":
            X += 1
        elif s == "W":
            Y += 1
        elif s == "S":
            X -= 1
        else:
            Y -= 1
        D.add(X*INF + Y)
        # print(X, Y, D)
        if ((R+X)*INF + C+Y) in D:
            ans[i] = 1
    print("".join(map(str, ans)))


if __name__ == "__main__":
    main()
