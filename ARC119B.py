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


def main():
    N = NI()
    S = SI()
    T = SI()

    if S.count("1") != T.count("1"):
        print(-1)
        exit()

    s1 = 0
    t1 = 0
    ans = 0
    for s, t in zip(S, T):
        if s == t == "0":
            if s1 > t1 or s1 < t1:
                ans += 1
        elif s == "0" and t == "1":
            if s1 > t1:
                s1 -= 1
                ans += 1
            else:
                t1 += 1
        elif s == "1" and t == "0":
            if s1 < t1:
                t1 -= 1
                ans += 1
            else:
                s1 += 1
        else:
            pass
    print(ans)


if __name__ == "__main__":
    main()
