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
    X = SLI()
    for a in range(3):
        for b in range(3):
            for c in range(3):
                if a == b or b == c or c == a:
                    continue
                if a < b and X[0] == ">":
                    continue
                elif a > b and X[0] == "<":
                    continue
                if a < c and X[1] == ">":
                    continue
                elif a > c and X[1] == "<":
                    continue
                if b < c and X[2] == ">":
                    continue
                elif b > c and X[2] == "<":
                    continue
                if a == 1:
                    print("A")
                elif b == 1:
                    print("B")
                else:
                    print("C")



if __name__ == "__main__":
    main()
