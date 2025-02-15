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
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    C = {alphabets[i]: NI() for i in range(26)}
    ans = C["h"] * C["e"] * C["w"] * C["d"] * C["r"]
    l = C["l"]
    tmp = 0
    for kl in range(2, l):
        kr = l - kl
        tmp = max(tmp, kl * (kl-1) // 2 * kr)
    ans *= tmp
    o = C["o"]
    ans *= o//2 * (o-o//2)
    print(ans)


if __name__ == "__main__":
    main()
