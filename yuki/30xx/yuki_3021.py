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
        S = SI()
        ans = solve(S)
        print(ans)


def solve(S):
    S = list(S)
    minus = False
    for i in range(len(S)):
        if S[i] == "-":
            minus = True
        elif S[i] == "+":
            minus = False
        elif S[i] == "?":
            if i == 0:
                S[i] = "9"
            elif minus:
                if S[i - 1] == "-" or i == len(S) - 1:
                    S[i] = "1"
                elif S[i + 1] == "+" or S[i + 1] == "-":
                    S[i] = "1"
                else:
                    S[i] = "+"
                    minus = False
            else:
                S[i] = "9"
    return "".join(S)


if __name__ == "__main__":
    main()
