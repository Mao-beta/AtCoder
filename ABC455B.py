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
    H, W = NMI()
    S = [SI() for _ in range(H)]
    ans = 0
    for h1 in range(H):
        for h2 in range(h1+1, H+1):
            for w1 in range(W):
                for w2 in range(w1+1, W+1):
                    ok = True
                    for i in range(h1, h2):
                        for j in range(w1, w2):
                            if S[i][j] != S[h1+h2-i-1][w1+w2-j-1]:
                                ok = False
                    ans += int(ok)
    print(ans)


if __name__ == "__main__":
    main()
