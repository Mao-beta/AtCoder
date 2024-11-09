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
    R = SI()
    C = SI()
    Rs = {s: set() for s in "ABC"}
    for P in permutations("ABC"+"."*(N-3)):
        l = "."
        for s in P[::-1]:
            if s != ".":
                l = s
        Rs[l].add("".join(P))

    for X in product(*[Rs[r] for r in R]):
        Xt = ["".join(x) for x in zip(*X)]
        ok = True
        for c, xt in zip(C, Xt):
            if xt not in Rs[c]:
                ok = False
        if ok:
            print("Yes")
            print(*X, sep="\n")
            return

    print("No")


if __name__ == "__main__":
    main()
