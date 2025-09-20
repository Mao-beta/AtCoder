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

import time
from random import randint

def main():
    N = NI()
    XY = EI(N)
    START = time.time()
    while time.time() - START < 1.5:
        i = randint(0, N - 1)
        j = randint(0, N - 1)
        if i == j:
            continue
        xi, yi = XY[i]
        xj, yj = XY[j]
        cnt = 0
        a = -(yj-yi)
        b = (xj-xi)
        c = xi*yj - xj*yi
        for x, y in XY:
            if a*x + b*y + c == 0:
                cnt += 1
        if cnt > N/2:
            print("Yes")
            print(a, b, c)
            return
    print("No")


if __name__ == "__main__":
    main()
