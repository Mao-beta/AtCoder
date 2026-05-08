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

from typing import List
from itertools import groupby

# RUN LENGTH ENCODING str -> list(tuple())
# example) "aabbbbaaca" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)]
def runLengthEncode(S: str) -> list[list[str, int]]:
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append([k, int(len(list(v)))])
    return res

def main():
    T = NI()
    for _ in range(T):
        A = SI()
        B = SI()
        RA = runLengthEncode(A)
        RB = runLengthEncode(B)
        a = []
        b = []
        for i, (c, k) in enumerate(RA):
            if 1 <= i < len(RA)-1 and c == "x" and k == 2 and RA[i-1][0] == "(" and RA[i+1][0] == ")":
                x = min(RA[i-1][1], RA[i+1][1])
                RA[i-1][1] -= x
                RA[i+1][1] -= x
        for i, (c, k) in enumerate(RB):
            if 1 <= i < len(RB)-1 and c == "x" and k == 2 and RB[i-1][0] == "(" and RB[i+1][0] == ")":
                x = min(RB[i-1][1], RB[i+1][1])
                RB[i-1][1] -= x
                RB[i+1][1] -= x
        for c, k in RA:
            if k > 0:
                a.append(c*k)
        for c, k in RB:
            if k > 0:
                b.append(c*k)
        if "".join(a) == "".join(b):
            print("Yes")
        else:
            print("No")
        

if __name__ == "__main__":
    main()
