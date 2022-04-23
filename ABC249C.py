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


alp_to_num = {chr(i+97): i for i in range(26)}


def main():
    N, K = NMI()
    S = [[alp_to_num[s] for s in SI()] for _ in range(N)]

    ans = 0

    for case in range(1<<N):
        num = bin(case).count("1")
        if num < K:
            continue

        ok = 0
        for s in range(26):
            tmp = 0
            for i in range(N):
                if (case >> i) & 1 == 0:
                    continue
                if s in S[i]:
                    tmp += 1
            if tmp == K:
                ok += 1

        ans = max(ans, ok)

    print(ans)


if __name__ == "__main__":
    main()
