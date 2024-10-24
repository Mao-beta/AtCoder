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
    S = [ord(s) - ord("A") for s in S]
    L = Counter()
    R = Counter(S[1:])
    N = len(S)
    ans = 0
    for i in range(N-1):
        for s in range(26):
            ans += L[s] * R[s]
        L[S[i]] += 1
        R[S[i+1]] -= 1
    print(ans)


if __name__ == "__main__":
    main()
