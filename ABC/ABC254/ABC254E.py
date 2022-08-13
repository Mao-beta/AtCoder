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


def adjlist_nond(n, edges):
    res = [[] for _ in range(n+1)]
    for a, b in edges:
        res[a].append(b)
        res[b].append(a)
    return res


def main():
    N, M = NMI()
    AB = [NLI() for _ in range(M)]
    Q = NI()
    XK = [NLI() for _ in range(Q)]

    G = adjlist_nond(N, AB)

    for x, k in XK:
        que = deque()
        ans = 0
        que.append((x, 0))
        seen = {x}
        while que:
            now, d = que.popleft()
            # print(now, d)
            if d > k:
                continue
            else:
                ans += now

            for goto in G[now]:
                if goto in seen:
                    continue
                seen.add(goto)
                que.append((goto, d+1))

        print(ans)


if __name__ == "__main__":
    main()
