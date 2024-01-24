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
    M = N-1
    UV = EI(N-1)
    UV = [[x-1, y-1] for x, y in UV]
    G = [[] for _ in range(N+M)]
    for i, (u, v) in enumerate(UV, start=N):
        G[u].append(i)
        G[i].append(u)
        G[v].append(i)
        G[i].append(v)

    N += M

    def bfs(start):
        steps = [-1] * N
        que = deque()
        que.append(start)
        steps[start] = 0
        while que:
            now = que.popleft()
            step = steps[now]
            for goto in G[now]:
                if steps[goto] != -1:
                    continue
                que.append(goto)
                steps[goto] = step + 1
        return steps

    steps = bfs(0)
    li = steps.index(max(steps))

    steps_li = bfs(li)
    li2 = steps_li.index(max(steps_li))

    steps_li2 = bfs(li2)
    r = max(steps_li2) // 2

    cent = -1
    for i, (s, s2) in enumerate(zip(steps_li, steps_li2)):
        if s == s2 == r:
            cent = i
            break

    def bfs2(start):
        que = deque()
        que.append(start)
        steps[start] = 1
        res = 0
        while que:
            now = que.popleft()
            step = steps[now]
            if step == r:
                res += 1
            for goto in G[now]:
                if steps[goto] != -1:
                    continue
                que.append(goto)
                steps[goto] = step + 1
        return res

    nums = []
    steps = [-1] * N
    steps[cent] = 0
    for g in G[cent]:
        nums.append(bfs2(g))

    ans = 1
    for num in nums:
        ans = ans * (num+1) % MOD99
    ans -= 1
    ans -= sum(nums)
    ans %= MOD99
    print(ans)


if __name__ == "__main__":
    main()
