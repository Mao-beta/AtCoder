import sys
import math
from collections import defaultdict
from collections import deque
from heapq import heapify, heappop, heappush

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


#隣接リスト 入力1-index を 0-index に
def adjlist_nond_1to0(n, edges):
    res = [[] for _ in range(n)]
    for a, b, c in edges:
        a, b = a-1, b-1
        res[a].append([b, c])
        res[b].append([a, c])
    return res


def main():
    N, M, Q = NMI()
    edges = [NLI() for _ in range(M)]
    X = NLI()

    graph = adjlist_nond_1to0(N, edges)

    ans = 1
    roads = []
    heapify(roads)
    for goto, c in graph[0]:
        heappush(roads, [c, goto])

    seen = [0] * N
    seen[0] = 1
    is_stable = False
    prev_x = 0
    for x in X:
        if is_stable and x <= prev_x:
            print(ans)
            continue

        is_stable = True

        new_cities = set()
        while roads:
            cost, city = heappop(roads)
            if cost > x:
                heappush(roads, [cost, city])
                break
            if seen[city]:
                continue
            new_cities.add(city)
        for city in new_cities:
            for goto, c in graph[city]:
                if seen[goto]: continue
                if goto in new_cities: continue
                heappush(roads, [c, goto])
            seen[city] = 1
            ans += 1
            is_stable = False
        print(ans)


if __name__ == "__main__":
    main()
