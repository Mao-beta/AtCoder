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
    N, M = NMI()
    S = [SI() for _ in range(N)]
    T = [
        "###.?????",
        "###.?????",
        "###.?????",
        "....?????",
        "?????????",
        "?????....",
        "?????.###",
        "?????.###",
        "?????.###"
    ]
    ans = []
    for h in range(N+1-9):
        for w in range(M+1-9):
            ok = True
            for i in range(9):
                for j in range(9):
                    s = S[h+i][w+j]
                    t = T[i][j]
                    if t == "?":
                        continue
                    if t != s:
                        # print(h, w, i, j, s, t)
                        ok = False
            if ok:
                ans.append([h+1, w+1])

    for h, w in ans:
        print(h, w)


if __name__ == "__main__":
    main()
