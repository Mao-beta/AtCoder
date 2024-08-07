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
    B = NLI()
    Q = NI()
    XY = EI(Q)
    S = set(A + B)
    import random
    H = {x: random.randint(1<<20, 1<<31) for x in S}
    ZA = [0]
    ZB = [0]
    SA = set()
    for a in A:
        if a not in SA:
            SA.add(a)
            ZA.append(ZA[-1] ^ a ^ H[a])
        else:
            ZA.append(ZA[-1])
    SB = set()
    for b in B:
        if b not in SB:
            SB.add(b)
            ZB.append(ZB[-1] ^ b ^ H[b])
        else:
            ZB.append(ZB[-1])
    for x, y in XY:
        if ZA[x] == ZB[y]:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
