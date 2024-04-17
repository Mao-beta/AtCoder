import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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
    D = NI()
    C = "x"*14 + SI() + SI() + "x"*14
    R = runLengthEncode(C)
    ans = 0
    for i, (x, k) in enumerate(R):
        i = int(i)
        if x == "x":
            if k <= D:
                tmp = k
                if i > 0:
                    tmp += R[i-1][1]
                if i < len(R)-1:
                    tmp += R[i+1][1]
                ans = max(ans, tmp)
            else:
                if i > 0:
                    ans = max(ans, D + R[i-1][1])
                if i < len(R) - 1:
                    ans = max(ans, D + R[i+1][1])
    if ans == 0:
        ans = D
    print(ans)


if __name__ == "__main__":
    main()
