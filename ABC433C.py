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
def runLengthEncode(S: str):
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((int(k), int(len(list(v)))))
    return res


def main():
    S = SI()
    R = runLengthEncode(S)
    ans = 0
    for i, (k, v) in enumerate(R[:-1]):
        k2, v2 = R[i+1]
        if k+1 == k2:
            x = min(v, v2)
            ans += x
    print(ans)


if __name__ == "__main__":
    main()
