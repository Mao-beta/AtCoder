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
    N, M = NMI()
    AB = [NLI() for _ in range(M)]
    D = [[0]*N for _ in range(N)]
    for a, b in AB:
        a -= 1
        b -= 1
        D[a][b] = 1
        D[b][a] = 1

    is_clique = [0] * (1<<N)
    for case in range(1<<N):
        S = []
        for v in range(N):
            if (case >> v) & 1:
                S.append(v)

        is_c = 1
        for i in range(len(S)):
            for j in range(i+1, len(S)):
                if D[S[i]][S[j]] == 0:
                    is_c = 0

        is_clique[case] = is_c

    # print(is_clique)
    # まだ使っていない点の集合sについて、その個数の最小値
    INF = 1000
    dp = [INF] * (1<<N)
    dp[-1] = 0
    for case in range((1<<N)-1, -1, -1):
        now = case
        d = dp[case]
        while now > 0:
            if not is_clique[now]:
                now = (now - 1) & case
                continue

            # print(now, case, now^case, d)
            # print(dp)
            dp[case ^ now] = min(dp[case ^ now], d+1)
            now = (now - 1) & case

    print(dp[0])


if __name__ == "__main__":
    main()
