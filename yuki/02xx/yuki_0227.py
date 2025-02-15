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
    A = sorted(NLI())
    C = Counter(A)
    if len(C) == 2 and set(C.values()) == {2, 3}:
        print("FULL HOUSE")
    elif 3 in C.values():
        print("THREE CARD")
    elif list(C.values()).count(2) == 2:
        print("TWO PAIR")
    elif list(C.values()).count(2) == 1:
        print("ONE PAIR")
    else:
        print("NO HAND")


if __name__ == "__main__":
    main()
