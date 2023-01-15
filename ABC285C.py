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
    S = SI()
    N = len(S)
    ans = 0
    for i in range(1, N):
        ans += 26**i

    S = [ord(s) - ord("A") for s in S]
    d = 1
    for s in S[::-1]:
        ans += s * d
        d *= 26

    print(ans+1)


if __name__ == "__main__":
    main()
