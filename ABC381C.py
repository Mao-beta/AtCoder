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
def runLengthEncode(S: str) -> "List[tuple[str, int]]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res


def main():
    N = NI()
    S = SI()
    ans = 1
    T = [runLengthEncode(s) for s in S.split("/")]
    for i in range(len(T)-1):
        R1, R2 = T[i], T[i+1]
        if len(R1) == 0 or len(R2) == 0:
            continue
        s1, k1 = R1[-1]
        s2, k2 = R2[0]
        if s1 == "1" and s2 == "2":
            ans = max(ans, min(k1, k2) * 2 + 1)
    print(ans)


if __name__ == "__main__":
    main()