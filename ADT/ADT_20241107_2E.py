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
    P = EI(4)
    for i in range(4):
        px, py = P[i]
        qx, qy = P[(i+1)%4]
        rx, ry = P[(i+2)%4]
        ux, uy = px-qx, py-qy
        vx, vy = rx-qx, ry-qy
        if vx*uy - vy*ux < 0:
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    main()
