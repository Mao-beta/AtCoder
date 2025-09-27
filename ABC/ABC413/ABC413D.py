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
    T = NI()
    for _ in range(T):
        N = NI()
        A = NLI()
        if N == 2:
            print("Yes")
            continue
        A.sort(key=lambda x: abs(x))
        if abs(A[0]) == abs(A[-1]):
            p, m = 0, 0
            for a in A:
                if a > 0:
                    p += 1
                else:
                    m += 1
            if abs(p-m) <= 1 or p == 0 or m == 0:
                print("Yes")
                continue
            else:
                print("No")
                continue
        else:
            ok = True
            for i in range(1, N-1):
                if A[i-1] * A[i+1] != A[i] ** 2:
                    ok = False
            if ok:
                print("Yes")
            else:
                print("No")


if __name__ == "__main__":
    main()
