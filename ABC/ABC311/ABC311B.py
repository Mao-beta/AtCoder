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


def main():
    N, D = NMI()
    S = [SI() for _ in range(N)]
    X = [1] * D
    for i in range(D):
        for j in range(N):
            if S[j][i] == "x":
                X[i] = 0

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

    R = runLengthEncode(X)
    ans = 0
    for s, k in R:
        if s == 1:
            ans = max(ans, k)

    print(ans)


if __name__ == "__main__":
    main()
