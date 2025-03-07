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
    S = SI()
    R = runLengthEncode(S)
    R.append(("", 0))
    ans = []
    ng = set()
    for i in range(len(R)-1):
        if i in ng:
            continue
        s1, k1 = R[i]
        s2, k2 = R[i+1]
        if s1 == "W" and s2 == "A":
            ans.append("A")
            ans.append("C" * k1)
            ans.append("A" * (k2-1))
            ng.add(i+1)
        else:
            ans.append(s1 * k1)
    print("".join(ans))


if __name__ == "__main__":
    main()
