import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
def runLengthEncode(S: str) -> "List[tuple[str, int]]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res


def solve(N, S):
    if "oo-" in S:
        return True
    if "-oo" in S:
        return True
    if "ooo" in S:
        return True
    if "o-o" in S:
        return True
    if "--o-" in S:
        return True
    if "-o--" in S:
        return True

    R = runLengthEncode(S)
    for i in range(1, len(R)-1):
        if R[i-1][0] == R[i+1][0] == "o" and R[i][0] == "-" and R[i][1] % 2:
            return True
    return False


def main():
    T = NI()
    for _ in range(T):
        N, S = SMI()
        if solve(N, S):
            print("O")
        else:
            print("X")


if __name__ == "__main__":
    main()
