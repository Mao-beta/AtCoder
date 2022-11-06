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
    N = NI()
    A = NLI()
    Two = []
    Three = []
    R = []
    for a in A:
        two = 0
        three = 0
        while a % 2 == 0:
            a //= 2
            two += 1
        while a % 3 == 0:
            a //= 3
            three += 1
        Two.append(two)
        Three.append(three)
        R.append(a)

    if len(set(R)) != 1:
        print(-1)
        exit()

    two_m = min(Two)
    three_m = min(Three)
    ans = sum(Two) + sum(Three) - (two_m + three_m) * N
    print(ans)


if __name__ == "__main__":
    main()
