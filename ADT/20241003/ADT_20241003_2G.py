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
    XYP = EI(N)
    D = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            xi, yi, pi = XYP[i]
            xj, yj, pj = XYP[j]
            d2 = abs(xi-xj) + abs(yi-yj)
            D[i][j] = (d2 + pi-1) // pi
    ans = 10**10
    for s in range(N):
        def judge(X):
            S = set()
            S.add(s)
            que = deque()
            que.append(s)
            while que:
                now = que.popleft()
                for goto in range(N):
                    if D[now][goto] <= X and goto not in S:
                        S.add(goto)
                        que.append(goto)
            return len(S) >= N

        ok = 10**11
        ng = 0
        while abs(ok - ng) > 1:
            X = (ok + ng) // 2
            if judge(X):
                ok = X
            else:
                ng = X

        # print(s, ok)
        ans = min(ans, ok)
    # print(*D, sep="\n")
    print(ans)


if __name__ == "__main__":
    main()
