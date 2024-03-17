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
    K = NI()
    XY = EI(K)
    XY = [[x-1, y-1] for x, y in XY]
    A = list(range(N))
    for x, y in XY:
        A[x], A[y] = A[y], A[x]

    seen = [0] * N
    C = []
    for s in range(N):
        if seen[s]:
            continue
        cnt = 0
        while not seen[s]:
            cnt += 1
            seen[s] = 1
            s = A[s]
        C.append(cnt)

    print(math.lcm(*C))


if __name__ == "__main__":
    main()
