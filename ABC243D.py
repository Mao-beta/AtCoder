import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

if "PyPy" in sys.version:
    import pypyjit

    pypyjit.set_param('max_unroll_recursion=-1')

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
    N, X = NMI()
    S = SI()

    T = deque()
    for s in S:
        if not T:
            T.append(s)
            continue

        x = T.pop()
        if x != "U" and s == "U":
            continue

        T.append(x)
        T.append(s)

    while T:
        s = T.popleft()
        if s == "U":
            X >>= 1
        elif s == "L":
            X <<= 1
        else:
            X <<= 1
            X |= 1
    print(X)


if __name__ == "__main__":
    main()
