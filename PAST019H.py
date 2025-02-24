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
    N, S = NMI()
    A = NLI()
    for B in permutations(A):
        for C in product("+*", repeat=N-1):
            s = []
            for b, c in zip(B, C):
                s.append(str(b))
                s.append(c)
            s.append(str(B[-1]))
            s = "".join(s)
            if eval(s) == S:
                print("Yes")
                print(s.replace("*", "x"))
                return
    print("No")


if __name__ == "__main__":
    main()
