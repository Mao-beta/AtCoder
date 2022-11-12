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


def main():
    N = NI()
    AB = [NLI() for _ in range(N)]
    G = defaultdict(list)
    for a, b in AB:
        G[a].append(b)
        G[b].append(a)

    S = set()
    que = deque()
    que.append(1)
    S.add(1)
    ans = 1
    while que:
        now = que.popleft()
        ans = max(ans, now)

        for goto in G[now]:
            if goto in S:
                continue
            S.add(goto)
            que.append(goto)

    print(ans)


if __name__ == "__main__":
    main()
