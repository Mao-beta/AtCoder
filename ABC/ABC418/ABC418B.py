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
    S = SI()
    L = len(S)
    ans = 0
    for i in range(L):
        for j in range(i + 3, L+1):
            T = S[i:j]
            if T[0] == T[-1] == "t":
                p = ((T.count("t")-2) / (j-i-2))
                ans = max(ans, p)
    print(ans)


if __name__ == "__main__":
    main()
