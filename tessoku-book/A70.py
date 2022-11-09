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
    N, M = NMI()
    A = NLI()
    XYZ = [NLI() for _ in range(M)]
    XYZ = [[x-1, y-1, z-1] for x, y, z in XYZ]
    moves = [(1<<x) | (1<<y) | (1<<z) for x, y, z in XYZ]

    steps = [-1] * (1<<N)
    start = 0
    for i, a in enumerate(A):
        start |= (1<<i) * a

    que = deque()
    que.append(start)
    steps[start] = 0

    while que:
        now = que.popleft()
        for mov in moves:
            goto = now ^ mov
            if steps[goto] != -1:
                continue
            steps[goto] = steps[now] + 1
            que.append(goto)

    print(steps[(1<<N)-1])


if __name__ == "__main__":
    main()
