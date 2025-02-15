import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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
    P = [int(s) for s in SI()]
    if len(P) == 1:
        print("No")
        return
    if P[-1] not in [2, 3, 4]:
        print("No")
        return
    a0 = False
    b0 = False
    up = 0
    for p in P[::-1]:
        ok = False
        for a in [0, 6, 7]:
            for b in [0, 6, 7]:
                if a0 and a != 0:
                    continue
                if b0 and b != 0:
                    continue
                if p == (a + b + up) % 10:
                    ok = True
                    if a == 0:
                        a0 = True
                    if b == 0:
                        b0 = True
                    up = (a + b + up) // 10
                    # print(a, b, up, p)
        if not ok:
            print("No")
            return
    if up:
        print("No")
        return
    print("Yes")


if __name__ == "__main__":
    main()
