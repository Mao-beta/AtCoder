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


def print_err(*args):
    print(*args, file=sys.stderr)


def main():
    N = NI()
    S = set()
    for a in range(1, 10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    for e in range(10):
                        for f in range(10):
                            a, b, c, d, e, f = map(str, [a, b, c, d, e, f])
                            s = a+a+b+c+d+d+e+f+e
                            s = int(s)
                            S.add(s)
    S = sorted(list(S))
    print(S[N-1])


if __name__ == "__main__":
    main()
