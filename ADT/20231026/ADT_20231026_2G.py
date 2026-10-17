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
EI = lambda m: [NLI() for _ in range(m)]


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
    N, X = NMI()
    S = SI()
    X = deque(runLengthEncode(bin(X)[2:]))
    for s in S:
        x, k = X.pop()
        if s == "U":
            k -= 1
            if k >= 1:
                X.append([x, k])
        elif s == "L":
            if x == "0":
                X.append([x, k+1])
            else:
                X.append([x, k])
                X.append(["0", 1])
        else:
            if x == "1":
                X.append([x, k+1])
            else:
                X.append([x, k])
                X.append(["1", 1])

    ans = []
    for x, k in list(X):
        for _ in range(k):
            ans.append(x)

    ans = int("".join(ans), 2)
    print(ans)


if __name__ == "__main__":
    main()
