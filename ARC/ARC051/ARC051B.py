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
    K = NI()
    F = [1, 1]
    for _ in range(40):
        F.append(F[-1] + F[-2])

    def gcd(a, b):
        if b == 0:
            return a
        C[0] += 1
        return gcd(b, a%b)

    for i in range(len(F)-1):
        C = [0]
        gcd(F[i], F[i+1])
        if C[0] == K:
            print(F[i], F[i+1])


if __name__ == "__main__":
    main()
