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
    N = len(S)
    L = []
    l = 0
    for i in range(1, N):
        if S[i] == S[i-1]:
            L.append(i-l)
            l = i
    L.append(N-l)
    ans = 0
    for l in L:
        ans += (l+1) * l // 2
        ans %= MOD99
    print(ans)


if __name__ == "__main__":
    main()
