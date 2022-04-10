import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

if "PyPy" in sys.version:
    import pypyjit

    pypyjit.set_param('max_unroll_recursion=-1')

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


from typing import List
from itertools import groupby

# RUN LENGTH ENCODING str -> list(tuple())
# example) "aabbbbaaca" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)]
def runLengthEncode(S: str) -> "List[List[str, int]]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append([k, int(len(list(v)))])
    return res


def main():
    N = NI()
    A = NLI()
    l = 0
    r = N
    b = 0
    while l < r:
        while A[r-1] == b:
            r -= 1
            if l >= r:
                print("Yes")
                exit()

        if A[l] == b:
            b = 1 - b
        else:
            print("No")
            exit()

        l += 1

    if l >= r:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
