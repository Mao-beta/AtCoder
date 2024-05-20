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
    l, r = NMI()
    ans = []
    d = 1
    while l < r:
        if l & 1:
            ans.append([l*d, (l+1)*d])
            l += 1
        if r & 1:
            ans.append([(r-1)*d, r*d])
            r -= 1
        l >>= 1
        r >>= 1
        d <<= 1
    ans.sort()
    print(len(ans))
    for l, r in ans:
        print(l, r)


if __name__ == "__main__":
    main()
