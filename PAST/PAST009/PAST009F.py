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
    A, B = NMI()
    S = [SI() for _ in range(3)]
    D = []
    for i in range(3):
        for j in range(3):
            if S[i][j] == "#":
                D.append([i-1, j-1])

    A, B = A-1, B-1
    seen = [[0]*9 for _ in range(9)]

    que = deque()
    que.append((A, B))
    seen[A][B] = 1
    while que:
        x, y = que.popleft()
        for dx, dy in D:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= 9 or ny < 0 or ny >= 9:
                continue
            if seen[nx][ny]:
                continue
            seen[nx][ny] = 1
            que.append((nx, ny))

    ans = 0
    for i in range(9):
        ans += sum(seen[i])
    print(ans)


if __name__ == "__main__":
    main()
