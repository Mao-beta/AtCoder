import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

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
    AB = EI(N)
    zero = 0
    C1 = Counter()
    C2 = Counter()
    for a, b in AB:
        if a == b == 0:
            zero += 1
            continue
        if b < 0 or (b == 0 and a < 0):
            a, b = -a, -b
        g = math.gcd(a, b)
        a //= g
        b //= g
        if a > 0:
            C1[(a, b)] += 1
        else:
            C2[(b, -a)] += 1

    tmp = 1
    for ab, k1 in C1.items():
        k2 = C2[ab]
        tmp *= (pow(2, k1, MOD) + pow(2, k2, MOD) - 1) % MOD
        tmp %= MOD
    for ab, k2 in C2.items():
        k1 = C1[ab]
        if k1 == 0:
            tmp *= pow(2, k2, MOD)
            tmp %= MOD

    tmp += zero
    tmp %= MOD

    print((tmp-1) % MOD)


if __name__ == "__main__":
    main()
