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
    Q = NI()
    ABC = EI(Q)
    V, E, F = set(), set(), set()
    INF = 10**9
    for a, b, c in ABC:
        V.add(a)
        V.add(b)
        V.add(c)
        E.add(INF*a + b)
        E.add(INF*b + c)
        E.add(INF*a + c)
        F.add(INF*INF*a + INF*b + c)
    print(len(V) - len(E) + len(F))


if __name__ == "__main__":
    main()
