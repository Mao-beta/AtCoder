import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

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
def runLengthEncode(S: str) -> "List[tuple[str, int]]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res


def main():
    S = SI()
    T = SI()
    RS = runLengthEncode(S)
    RT = runLengthEncode(T)

    if len(RS) != len(RT):
        print("No")
        exit()

    for (s, ks), (t, kt) in zip(RS, RT):
        if s != t:
            print("No")
            exit()

        if ks > kt:
            print("No")
            exit()

        elif ks == kt:
            continue

        elif ks == 1:
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()
