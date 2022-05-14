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
    N = NI()
    names = [SI().split() for _ in range(N)]

    for i, (s, t) in enumerate(names):
        s_ok = True
        t_ok = True
        for j in range(N):
            ss, tt = names[j]
            if i == j: continue
            if s == ss or s == tt:
                s_ok = False
            if t == tt or t == ss:
                t_ok = False
        if not s_ok and not t_ok:
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()
