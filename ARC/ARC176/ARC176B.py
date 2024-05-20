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
        N, M, K = NMI()

        if M == 2:
            print(0)
            continue
        if M-K == 1:
            # 2^N % 2^K
            # N>=Kのときあまり0
            # そうでないとき2^Nのあまり
            if N >= K:
                print(0)
            else:
                print(pow(2, N, 10))
            continue

        # 割る数は2^(M-1)より大きい
        if N <= M-1:
            print(pow(2, N, 10))
            continue

        r = (N-K) % (M-K)
        print(pow(2, r, 10) * pow(2, K, 10) % 10)


if __name__ == "__main__":
    main()
