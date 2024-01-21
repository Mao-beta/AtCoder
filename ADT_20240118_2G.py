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
    S = SI()
    Q = NI()
    B = 63
    for _ in range(Q):
        t, k = NMI()
        k -= 1
        if t > B:
            k = bin(k)[2:]
            rem = t - len(k)
            s = (ord(S[0]) - ord("A")) % 3
            s = (s + rem) % 3
            for b in k:
                if b == "0":
                    s += 1
                else:
                    s -= 1
            s %= 3
            print(chr(ord("A") + s))

        else:
            P = pow(2, t)
            idx, k = divmod(k, P)

            k = bin(k)[2:]
            rem = t - len(k)
            s = (ord(S[idx]) - ord("A")) % 3
            s += rem
            s %= 3

            for b in k:
                if b == "0":
                    s += 1
                else:
                    s -= 1
            s %= 3
            print(chr(ord("A") + s))


if __name__ == "__main__":
    main()
