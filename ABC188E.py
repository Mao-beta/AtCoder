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

    min_prices = [10**10] * (N+1)
    min_idx = [i for i in range(N+1)]
    ans = -10**10
    for i in range(N+1):
        if i == 0: continue

        for goto in roads[i]:
            min_prices[goto] = min(min_prices[goto], A[i], min_prices[i])

    for i, (p, idx) in enumerate(zip(min_prices, min_idx)):
        if i == 0: continue
        ans = max(ans, A[i]-p)

    print(ans)




if __name__ == "__main__":
    main()
