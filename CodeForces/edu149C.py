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
    T = NI()
    for _ in range(T):
        S = SI()
        R = runLengthEncode(S)
        ans = []
        for i in range(len(R)):
            s, x = R[i]
            if s != "?":
                ans.append(s*x)
            else:
                prev = None
                nex = None
                if i > 0:
                    prev = R[i-1][0]
                if i < len(R)-1:
                    nex = R[i+1][0]

                ss = "0"
                if prev is None and nex is None:
                    pass
                elif prev is None:
                    ss = nex
                elif nex is None:
                    ss = prev
                elif nex == prev:
                    ss = nex
                else:
                    pass

                ans.append(ss*x)

        print("".join(ans))


if __name__ == "__main__":
    main()
