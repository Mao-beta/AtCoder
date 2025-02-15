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
    p = 129402307
    N = SI()
    M = SI()

    if N[0] == "0":
        print(0)
        return
    if M[0] == "0":
        print(1)
        return

    n = 0
    for s in N:
        n = (n*10+int(s)) % p

    m = 0
    for s in M:
        m = (m*10+int(s)) % (p-1)

    if n == 0:
        print(0)
        return
    if m == 0:
        print(1)
        return
    print(pow(n, m, p))


if __name__ == "__main__":
    main()
