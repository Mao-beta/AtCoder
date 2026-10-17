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
    N, T = NMI()
    AB = []
    ABI = []
    for i in range(N):
        a, b = NMI()
        AB.append([a, b])
        ABI.append([a, b, i])
    ABI.sort(key=lambda x: [-x[0], x[1], x[2]])
    A, B, _ = ABI[0]
    for a, b in AB:
        print(T * (A-a) + b-B)


if __name__ == "__main__":
    main()
