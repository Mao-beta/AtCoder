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


def nex(s, b):
    if b == 0:
        return (s + 1) % 3
    else:
        return (s + 2) % 3


def main():
    S = SI()
    Q = NI()

    D = {"A": 0, "B": 1, "C": 2}
    R = "ABC"
    S = [D[s] for s in S]

    for _ in range(Q):
        t, k = NMI()
        if t == 0:
            print(R[S[k-1]])
            continue

        k -= 1
        L = []
        while k > 0 and t >= 1:
            L.append(k % 2)
            k //= 2
            t -= 1

        if t > 0:
            now = (S[0] + t) % 3
        else:
            now = S[k]

        L = L[::-1]
        for l in L:
            now = nex(now, l)
        print(R[now])


if __name__ == "__main__":
    main()
