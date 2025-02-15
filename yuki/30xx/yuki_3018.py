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
    H, W = NMI()
    if H == 1 and W == 1:
        print("! 1 1", flush=True)
        exit()
    print(f"? 1 1", flush=True)
    d1 = NI()

    if H == 1:
        for w in range(1, W+1):
            c1 = (w-1)**2
            if c1 == d1:
                print(f"! 1 {w}", flush=True)
                exit()

    if W == 1:
        for h in range(1, H+1):
            c1 = (h-1)**2
            if c1 == d1:
                print(f"! {h} 1", flush=True)
                exit()

    print(f"? 1 {W}", flush=True)
    d2 = NI()
    for h in range(1, H+1):
        for w in range(1, W+1):
            c1 = (h-1)**2 + (w-1)**2
            c2 = (h-1)**2 + (w-W)**2
            if c1 == d1 and c2 == d2:
                print(f"! {h} {w}", flush=True)
                exit()


if __name__ == "__main__":
    main()
