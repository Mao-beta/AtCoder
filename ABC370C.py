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


def main():
    S = list(SI())
    T = list(SI())
    ans = []
    for i in range(len(S)):
        if S[i] <= T[i]:
            continue
        S[i] = T[i]
        ans.append("".join(S))
    for i in range(len(S)-1, -1, -1):
        if S[i] == T[i]:
            continue
        S[i] = T[i]
        ans.append("".join(S))
    print(len(ans))
    for s in ans:
        print(s)


if __name__ == "__main__":
    main()
