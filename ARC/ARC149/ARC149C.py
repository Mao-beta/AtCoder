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
    N = NI()
    ans = [[0] * N for _ in range(N)]

    if N % 2 == 0:
        x = 2
        for h in range(N//2, N):
            for w in range(N):
                ans[h][w] = x
                x += 2

        B = [set() for _ in range(3)]
        for x in range(1, N**2+1, 2):
            B[x%3].add(x)

        C = [1, 2, 0]
        now = 0

        for h in range(N//2-1, -1, -1):
            for w in range(N):
                if h == N//2-1:
                    x = B[C[w%3]].pop()
                    while x + ans[h+1][w] == 3:
                        B[C[w % 3]].add(x)
                        x = B[C[w % 3]].pop()
                    ans[h][w] = x
                else:
                    x = B[now].pop()
                    ans[h][w] = x
                    if not B[now]:
                        now += 1


    else:
        M = N//2
        A = [[5, 9, 1],[3, 7, 8],[6, 2, 4]]

        for h in range(M-1, M+2):
            for w in range(M-1, M+2):
                ans[h][w] = A[h-M+1][w-M+1]

        Odd = [set() for _ in range(3)]
        for x in range(11, N ** 2 + 1, 2):
            Odd[x % 3].add(x)

        Even = [set() for _ in range(3)]
        for x in range(10, N ** 2 + 1, 2):
            Even[x % 3].add(x)

        now = 0
        h = M
        for w in range(N):
            if w == M:
                h -= 1

            if ans[h][w] != 0:
                continue

            ev = Even[now].pop()
            od = Odd[(-now)%3].pop()
            ans[h][w] = od
            ans[h+1][w] = ev

            if not Even[now] or not Odd[(-now)%3]:
                now += 1

        now = 0
        for h in range(N):
            for w in range(N):
                if ans[h][w] != 0:
                    continue

                if not Odd[now]:
                    now += 1

                if now == 3:
                    break

                x = Odd[now].pop()
                ans[h][w] = x

            if now == 3:
                break

        now = 0
        for h in range(N):
            for w in range(N):
                if ans[h][w] != 0:
                    continue

                if not Even[now]:
                    now += 1

                if now == 3:
                    break

                x = Even[now].pop()
                ans[h][w] = x

            if now == 3:
                break


    for row in ans:
        print(*row)


if __name__ == "__main__":
    main()
