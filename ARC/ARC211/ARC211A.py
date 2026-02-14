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
    T = NI()
    for _ in range(T):
        A = [0] + NLI()
        if A[5] == 0:
            X = [i for i in range(10) if A[i]]
            if len(X) == 2 and sum(X) == 10:
                print(1)
            else:
                print(0)
        else:
            rest = sum(A) - A[5]
            if rest >= A[5]-1:
                print(0)
            else:
                print(A[5]-1 - rest)


if __name__ == "__main__":
    main()
