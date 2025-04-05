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
    Q = NI()
    # aAAa
    X = [len(S)]
    while X[-1] < 10**18:
        X.append(X[-1] << 1)
    K = NLI()
    ans = []
    for k in K:
        k -= 1
        rev = 0
        for x in X[::-1]:
            if k >= x:
                rev ^= 1
                k -= x
        s = S[k]
        if rev:
            if s.islower():
                s = s.upper()
            else:
                s = s.lower()
        ans.append(s)
    print(*ans)


if __name__ == "__main__":
    main()
