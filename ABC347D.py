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
    a, b, C = NMI()
    c = C.bit_count()
    # print(a, b, c)
    X = 0
    Y = 0
    if (-a+b+c) % 2:
        print(-1)
        return
    if (a-b+c) % 2:
        print(-1)
        return
    if (a+b-c) % 2:
        print(-1)
        return
    if (a+b+c) % 2:
        print(-1)
        return

    if (-a+b+c) < 0:
        print(-1)
        return
    if (a-b+c) < 0:
        print(-1)
        return
    if (a+b-c) < 0:
        print(-1)
        return
    if (a+b+c) < 0:
        print(-1)
        return

    q = (a-b+c) // 2
    r = (-a+b+c) // 2
    s = (a+b-c) // 2
    p = 60 - q - r - s
    if p < 0 or p > 60:
        print(-1)
        return

    for i in range(60):
        b = 1 << i
        if (C >> i) & 1 == 0:
            if s > 0:
                X ^= b
                Y ^= b
                s -= 1
        else:
            if q > 0:
                X ^= b
                q -= 1
            elif r > 0:
                Y ^= b
                r -= 1
            else:
                print(-1)
                return

    print(X, Y)
    # print(X.bit_count(), Y.bit_count(), X^Y)


if __name__ == "__main__":
    main()
