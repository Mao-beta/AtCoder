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


def _main():
    N = NI()
    A = [SI() for _ in range(N)]
    Z = 0
    F = 0
    for S in A:
        if "." not in S:
            S += ".0"
        if S[0] != "-":
            z, f = S.split(".")
            z = int(z)
            f = f.ljust(10, "0")
            f = int(f)
        else:
            z, f = S.split(".")
            z = int(z)
            f = f.ljust(10, "0")
            f = -int(f)
        Z += z
        F += f
    x, r = divmod(F, 10**10)

    Z += x
    F = r
    if Z < 0 and F > 0:
        Z += 1
        F = 10**10 - F
        Z = "-" + str(abs(Z))
    print(f"{Z}.{str(F).zfill(10)}")


def main():
    N = NI()
    A = [SI() for _ in range(N)]
    X = []
    for i in range(N):
        a = A[i]
        if "." not in a:
            X.append(int(a) * 10**10)
        else:
            z, f = a.split(".")
            f = f.ljust(10, "0")
            X.append(int(z+f))
    # print(X)
    SX = sum(X)
    if SX < 0:
        ans = str(SX).zfill(12)
    else:
        ans = str(SX).zfill(11)
    print(str(ans[:-10]) + "." + str(ans)[-10:])


if __name__ == "__main__":
    main()
