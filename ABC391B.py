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
    N, M = NMI()
    S = [SI() for _ in range(N)]
    T = [SI() for _ in range(M)]

    def check(h, w):
        for i in range(h, h+M):
            for j in range(w, w+M):
                if S[i][j] != T[i-h][j-w]:
                    return False
        return True

    for h in range(N-M+1):
        for w in range(N-M+1):
            if check(h, w):
                print(h+1, w+1)
                exit()


if __name__ == "__main__":
    main()
