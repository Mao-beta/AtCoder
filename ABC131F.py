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
    XY = EI(N)
    XY = [[x-1, y-1] for x, y in XY]
    M = 10**5
    G = defaultdict(list)
    for x, y in XY:
        G[x].append(y+M)
        G[y+M].append(x)

    ans = 0
    seen = defaultdict(lambda: 0)
    for v in range(M):
        if seen[v]:
            continue

        xn = set()
        yn = set()
        que = deque()
        que.append(v)

        while que:
            now = que.popleft()
            seen[now] = 1
            if now < M:
                xn.add(now)
            else:
                yn.add(now)

            for goto in G[now]:
                if seen[goto]:
                    continue
                que.append(goto)

        ans += len(xn) * len(yn)

    print(ans - N)


if __name__ == "__main__":
    main()
