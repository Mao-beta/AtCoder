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
    N, K = NMI()
    S = list(SI())
    for i in range(N):
        if S[i] == "o":
            if i > 0:
                S[i-1] = "."
            if i < N-1:
                S[i+1] = "."
    R = runLengthEncode(S)
    able = 0
    for s, k in R:
        if s == "?":
            if k % 2 == 0:
                able += k // 2
            else:
                able += (k+1) // 2
    if K - S.count("o") == 0:
        for i in range(N):
            if S[i] == "?":
                S[i] = "."
        print("".join(S))
    elif able + S.count("o") == K:
        ans = []
        for s, k in R:
            # print(s, k)
            if s == "?" and k % 2:
                for i in range(k):
                    if i % 2 == 0:
                        ans.append("o")
                    else:
                        ans.append(".")
            else:
                for i in range(k):
                    ans.append(s)
        # print("#")
        print("".join(ans))
    else:
        print("".join(S))


if __name__ == "__main__":
    main()
