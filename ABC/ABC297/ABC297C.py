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
    H, W = NMI()
    ans = []
    for h in range(H):
        S = list(SI())
        for w in range(W-1):
            if S[w] == S[w+1] == "T":
                S[w] = "P"
                S[w+1] = "C"
        ans.append("".join(S))

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
