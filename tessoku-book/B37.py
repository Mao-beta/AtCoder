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


def main():
    Ns = SI().zfill(16)
    N = int(Ns)
    ans = 0
    for k in range(1, 16):
        b = int(Ns[:-k])
        p = 10**(k-1)
        y = int(Ns[-k])
        for x in range(10):
            if x < y:
                r = p
            elif x == y:
                if k == 1:
                    z = 0
                else:
                    z = int(Ns[-k+1:])

                r = z + 1
            else:
                r = 0
            # print(k, b, p, r, x)
            ans += (b * p + r) * x
    print(ans)


if __name__ == "__main__":
    main()
