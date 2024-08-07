import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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
    N, L, R = NMI()
    R += 1

    def question(i, j):
        print("?", i, j, flush=True)
        return NI()

    def answer(S):
        print("!", S, flush=True)

    B = 1 << N
    G = [[] for _ in range(B+1)]
    for i in range(N+1):
        p = 1 << i
        for j in range(B//p):
            l = p * j
            r = l + p
            G[l].append(r)
            G[r].append(l)

    # BFS
    steps = [-1] * (B+1)
    pars = [-1] * (B+1)
    que = deque()
    que.append(R)
    steps[R] = 0
    while que:
        now = que.popleft()
        step = steps[now]
        for goto in G[now]:
            if steps[goto] != -1:
                continue
            que.append(goto)
            pars[goto] = now
            steps[goto] = step + 1

    # print(steps)
    # print(pars)

    ans = 0
    now = L
    while now != R:
        goto = pars[now]
        # print(now, goto)
        d = abs(goto - now)
        i = 0
        while (d & 1) == 0:
            d >>= 1
            i += 1
        j = min(now, goto) // abs(goto - now)
        r = question(i, j)
        if now < goto:
            ans += r
        else:
            ans -= r
        now = goto

    answer(ans % 100)


if __name__ == "__main__":
    main()
