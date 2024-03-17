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
    N = NI()
    C = list(SI())
    if C[0] == "B":
        C = ["A" if c == "B" else "B" for c in C]

    cum = [0]
    for c in C[1:] + [C[0]]:
        if c == "A":
            cum.append(cum[-1] + 1)
        else:
            cum.append(cum[-1] - 1)

    ans = 1
    # print(cum)
    for x, c in zip(cum[1:], C[1:]):
        # print(x, c)
        if -2 <= x <= 0 and c == "B":
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
