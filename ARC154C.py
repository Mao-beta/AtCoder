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
def runLengthEncode(S: str) -> "List[tuple[str, int]]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append([k, int(len(list(v)))])
    return res


def solve(N, A, B):
    if A == B:
        return "Yes"

    AR = runLengthEncode(A)
    if len(AR) >= 2 and AR[0][0] == AR[-1][0]:
        AR[0][1] += AR[-1][1]
        AR.pop()
    AR2 = AR * 2
    BR = runLengthEncode(B)
    if len(BR) >= 2 and BR[0][0] == BR[-1][0]:
        BR[0][1] += BR[-1][1]
        BR.pop()

    for ai in range(len(AR)):
        ok = False
        corner = True

        idx = 0
        for i in range(ai, ai+len(AR)):
            # print(i)
            a, k = AR2[i]
            if k > 1:
                corner = False
            if a == BR[idx][0]:
                if BR[idx][1] > 1:
                    corner = False
                idx += 1
            else:
                corner = False

            if idx == len(BR):
                ok = True
                break

        if ok and not corner:
            return "Yes"

    return "No"


def main():
    T = NI()
    for _ in range(T):
        N = NI()
        A = NLI()
        B = NLI()
        ans = solve(N, A, B)
        print(ans)


def rand():
    from random import randint
    T = NI()
    for _ in range(T):
        N = 3
        A = [randint(1, 2) for _ in range(N)]
        B = [randint(1, 2) for _ in range(N)]
        print(A, B)
        ans = solve(N, A, B)

        print(ans)


if __name__ == "__main__":
    main()
    # rand()
