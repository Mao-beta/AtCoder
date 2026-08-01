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
    N = NI()
    ans = 0
    r = 2
    for l in range(1, N):
        if r <= l:
            r = l+1
        while r <= N:
            print(f"? {l} {r}", flush=True)
            res = SI()
            if res == "No":
                break
            else:
                r += 1
        ans += r-l-1

    print(f"! {ans}", flush=True)


if __name__ == "__main__":
    main()
