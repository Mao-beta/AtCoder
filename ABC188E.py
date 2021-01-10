import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def make_adjlist_d(n, edges):
    res = [[] for _ in range(n+1)]
    for edge in edges:
        res[edge[0]].append(edge[1])
    return res


def main():
    N, M = NMI()
    A = [10**10]+NLI()
    edges = [NLI() for _ in range(M)]
    roads = make_adjlist_d(N, edges)
    #print(roads)

    stack = deque()
    seen = set()
    ans = -10**10
    for start in range(1, N+1):
        if start in seen: continue

        stack.append((start, 10**10))
        while stack:
            now, buy = stack.pop()
            seen.add(now)
            ans = max(A[now]-buy, ans)
            towns = roads[now]
            for goto in towns:
                stack.append((goto, min(buy, A[now])))

    print(ans)





if __name__ == "__main__":
    main()
