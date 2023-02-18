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
        res.append((k, int(len(list(v)))))
    return res


def solve(N, S):
    one = S.count("1")
    if one % 2:
        return -1

    if one >= 4:
        return one // 2

    if one == 0:
        return 0

    if "11" not in S:
        return 1

    if N >= 5:
        return 2
    if N <= 3:
        return -1

    if S == "0110":
        return 3
    elif S in ["1100", "0011"]:
        return 2


def main():
    T = NI()
    for _ in range(T):
        N = NI()
        S = SI()
        ans = solve(N, S)
        print(ans)


if __name__ == "__main__":
    main()
