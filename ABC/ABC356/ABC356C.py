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
    N, M, K = NMI()
    oks = [1] * (1<<N)
    for _ in range(M):
        C, *A, R = SMI()
        A = list(map(int, A))
        for case in range(1<<N):
            if oks[case] == 0:
                continue
            k = 0
            for a in A:
                a -= 1
                if (case >> a) & 1:
                    k += 1
            if (k >= K and R == "x") or (k < K and R == "o"):
                oks[case] = 0
    print(sum(oks))


if __name__ == "__main__":
    main()
