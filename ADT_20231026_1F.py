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
    N = NI()
    G = [[] for _ in range(N)]
    T = []
    for i in range(N):
        t, k, *a = NMI()
        for ai in a:
            G[i].append(ai-1)
        T.append(t)

    steps = [-1] * N
    que = deque()
    que.append(N-1)
    steps[N-1] = 0
    while que:
        now = que.popleft()
        step = steps[now]
        for goto in G[now]:
            if steps[goto] != -1:
                continue
            que.append(goto)
            steps[goto] = step + 1

    ans = 0
    for i, s in enumerate(steps):
        if s >= 0:
            ans += T[i]
    print(ans)


if __name__ == "__main__":
    main()
