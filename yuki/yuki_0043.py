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
    S = [list(SI()) for _ in range(N)]

    ans = [N]

    def dfs(ij):
        i, j = divmod(ij, N)
        if ij >= N**2:
            W = [S[h].count("o") for h in range(N)]
            w = W[0]
            SW = sorted(list(set(W)), reverse=True)
            res = SW.index(w) + 1
            ans[0] = min(ans[0], res)
            return
        if i >= j or S[i][j] != "-":
            dfs(ij+1)
            return

        S[i][j] = "o"
        S[j][i] = "x"
        dfs(ij+1)

        S[i][j] = "x"
        S[j][i] = "o"
        dfs(ij+1)

        S[i][j] = "-"
        S[j][i] = "-"
        return

    dfs(0)
    print(ans[0])


if __name__ == "__main__":
    main()
