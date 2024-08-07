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
    N = NI()
    A = NLI()
    M = 200000
    C = [0] * (M+1)
    for a in A:
        C[a] += 1
    ans = 0
    for aj in range(1, (M+1)):
        for ak in range(1, (M+1)):
            if aj * ak > M:
                break
            ai = aj * ak
            ans += C[ai] * C[aj] * C[ak]
    print(ans)


if __name__ == "__main__":
    main()
