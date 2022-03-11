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

# sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD99 = 998244353

input = lambda: sys.stdin.readline().rstrip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())


def main():
    N, L = NMI()
    S = [SI() for _ in range(L)]
    T = input()
    # print(T)
    y = T.index("o")
    # print(y)
    for s in S[::-1]:
        if y >= 1 and s[y-1] == "-":
            y -= 2
        elif y < 2*N-2 and s[y+1] == "-":
            y += 2
        # print(y)
    print(y // 2 + 1)


if __name__ == "__main__":
    main()
