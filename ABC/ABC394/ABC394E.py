import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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
    C = [SI() for _ in range(N)]

    INF = 10**10
    ans = [INF] * (N*N)
    que = deque()
    for i in range(N):
        ans[i*N+i] = 0
        que.append(i*N+i)
    for i in range(N):
        for j in range(N):
            c = C[i][j]
            if c == "-":
                continue
            if ans[i*N+j] == INF:
                ans[i*N+j] = 1
                que.append(i*N+j)

    while que:
        ij = que.popleft()
        i, j = divmod(ij, N)

        for i2j2 in range(N*N):
            i2, j2 = divmod(i2j2, N)
            if C[i2][i] == C[j][j2] != "-":
                if ans[i2*N+j2] > ans[i*N+j] + 2:
                    ans[i2*N+j2] = ans[i*N+j] + 2
                    # print("next", i2, j2)
                    que.append(i2j2)

    # print(G)
    for i in range(N):
        row = [x if x < INF else -1 for x in ans[i*N:i*N+N]]
        print(*row)


if __name__ == "__main__":
    main()
