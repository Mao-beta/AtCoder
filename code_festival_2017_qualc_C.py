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


def main():
    S = SI()
    T = S.replace("x", "")

    if T != T[::-1]:
        print(-1)
        exit()

    RS = runLengthEncode(S)
    R = [0]
    for s, k in RS:
        if s == "x":
            R[-1] += k
        else:
            for i in range(k):
                R.append(0)

    ans = 0
    for x, y in zip(R, R[::-1]):
        ans += abs(x-y)

    print(ans // 2)


if __name__ == "__main__":
    main()
