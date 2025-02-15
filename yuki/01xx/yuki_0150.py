import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
    T = NI()
    for _ in range(T):
        S = SI()
        N = len(S)
        ans = 11
        ming = 4
        for i in range(N+1-11):
            G = S[i:i+4]
            tmp = 0
            for g, tg in zip(G, "good"):
                if g != tg:
                    tmp += 1
            ming = min(ming, tmp)
            for j in range(i+4, N+1-7):
                P = S[j:j+7]
                tmp = 0
                for p, tp in zip(P, "problem"):
                    if p != tp:
                        tmp += 1
                ans = min(ans, ming + tmp)
        print(ans)


if __name__ == "__main__":
    main()
