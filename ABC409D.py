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
    T = NI()
    for _ in range(T):
        N = NI()
        S = SI()
        l = -1
        r = N
        for i in range(N):
            if l == -1 and i < N-1 and S[i] > S[i+1]:
                l = i
            elif l == -1:
                continue
            elif S[i] <= S[l]:
                continue
            else:
                r = i
                break
        # print(l, r, S[:l], S[l+1:r], S[l:l+1], S[r:])
        if l == -1:
            print("".join(S))
            continue
        ans = S[:l] + S[l+1:r] + S[l:l+1] + S[r:]
        print("".join(ans))


def guchoku(N, S):
    ans = []
    for l in range(N):
        for r in range(l, N):
            pass


if __name__ == "__main__":
    main()
