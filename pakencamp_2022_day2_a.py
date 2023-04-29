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


def main():
    N, M = NMI()
    AB = EI(M)
    AB = [[x-1, y-1] for x, y in AB]
    D = [0] * N
    for a, b in AB:
        D[a] += 1
    ans = [i for i, d in enumerate(D, start=1) if d == 0]
    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    main()
