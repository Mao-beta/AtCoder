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
    M = NI()
    UV = [NLI() for _ in range(M)]
    P = [0] + NLI()
    state = [0] * 10
    for i, p in enumerate(P):
        state[p] = i

    INF = 10**15
    D = defaultdict(lambda: INF)

    que = deque()
    que.append(tuple(state))
    D[tuple(state)] = 0

    goal = list(range(10))
    goal[9] = 0
    goal = tuple(goal)

    while que:
        now_state = que.popleft()
        now_step = D[now_state]

        if now_state == goal:
            print(now_step)
            exit()

        for u, v in UV:
            state = list(now_state)

            if state[u] == 0 and state[v] > 0:
                state[u] = state[v]
                state[v] = 0
            elif state[u] > 0 and state[v] == 0:
                state[v] = state[u]
                state[u] = 0
            else:
                continue

            state = tuple(state)
            if D[state] < INF:
                continue

            D[state] = now_step + 1
            que.append(state)

    print(-1)


if __name__ == "__main__":
    main()
