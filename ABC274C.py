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
    graph = [[] for _ in range(2*N+5)]
    for i, a in enumerate(A, start=1):
        graph[a].append(2*i)
        graph[a].append(2*i+1)

    steps = [-1] * (2*N+5)
    que = deque()
    que.append(1)
    steps[1] = 0
    while que:
        now = que.popleft()
        step = steps[now]
        for goto in graph[now]:
            if steps[goto] != -1:
                continue
            que.append(goto)
            steps[goto] = step + 1

    print(*steps[1:2*N+2], sep="\n")


if __name__ == "__main__":
    main()
