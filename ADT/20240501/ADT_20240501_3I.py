import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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
    A = []
    S = []
    for _ in range(N):
        A.append(NI())
        S.append(NLI())
    # 1..M: 数, M+1..M+N: Set
    G = [[] for _ in range(N+M+1)]
    for si, SS in enumerate(S, start=M+1):
        for s in SS:
            G[si].append(s)
            G[s].append(si)

    steps = [-1] * (N+M+1)
    que = deque()
    que.append(1)
    steps[1] = 0
    while que:
        now = que.popleft()
        step = steps[now]
        for goto in G[now]:
            if steps[goto] != -1:
                continue
            que.append(goto)
            steps[goto] = step + 1
    if steps[M] < 0:
        print(-1)
    else:
        print(steps[M]//2-1)


if __name__ == "__main__":
    main()
