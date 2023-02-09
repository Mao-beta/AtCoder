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
    S = SI()
    K = NI()
    N = len(S)
    S = [ord(s) - ord("a") for s in S]
    for i in range(N):
        s = S[i]
        if (26 - s) % 26 > K:
            continue

        K -= (26 - s) % 26
        S[i] = 0

    if K > 0:
        S[-1] = (S[-1] + K) % 26

    S = [chr(s + ord("a")) for s in S]
    print("".join(S))


if __name__ == "__main__":
    main()
