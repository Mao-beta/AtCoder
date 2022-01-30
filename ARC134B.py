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
num_to_alp = {i: chr(i+97) for i in range(26)}


def main():
    N = NI()
    S = SI()
    S = [alp_to_num[s] for s in S]

    # ある文字sのindexのリストを各文字について保持
    ST = [[] for _ in range(26)]
    for i, s in enumerate(S):
        ST[s].append(i)

    # まだ交換していない範囲で最大のindex
    R = N-1
    for l in range(N):
        s = S[l]
        for i in range(s):
            is_ok = False

            while ST[i]:
                r = ST[i].pop()
                if r > R: continue
                if l >= r: continue
                S[l], S[r] = S[r], S[l]
                R = r-1
                is_ok = True
                break

            if is_ok:
                break

    print("".join([num_to_alp[i] for i in S]))


if __name__ == "__main__":
    main()
