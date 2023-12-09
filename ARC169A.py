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
    A = NLI()
    P = [0] + NLI()
    P = [x-1 for x in P]

    R = [[] for _ in range(N)]
    for i, p in enumerate(P):
        if i == 0:
            continue
        R[p].append(i)

    steps = [-1] * N
    que = deque()
    que.append(0)
    steps[0] = 0
    while que:
        now = que.popleft()
        step = steps[now]
        for goto in R[now]:
            if steps[goto] != -1:
                continue
            que.append(goto)
            steps[goto] = step + 1

    cum = [0] * N
    for i, s in enumerate(steps):
        cum[s] += A[i]

    for i in range(N-1, -1, -1):
        if cum[i] == 0:
            continue
        if cum[i] > 0:
            print("+")
            return
        elif cum[i] < 0:
            print("-")
            return

    print(0)


if __name__ == "__main__":
    main()
