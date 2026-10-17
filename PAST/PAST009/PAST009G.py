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
    N, Q = NMI()
    A = [[0]*N for _ in range(N)]


    def dfs(start, end):
        stack = deque()
        stack.append(start)
        seen = [0] * N
        seen[start] = 1

        while stack:
            now = stack.pop()
            for goto in range(N):
                if A[now][goto] == 0:
                    continue
                if seen[goto]:
                    continue
                if goto == end:
                    return True
                stack.append(goto)
                seen[goto] = 1

        return False


    for _ in range(Q):
        q, u, v = NMI()
        u, v = u-1, v-1
        if q == 1:
            A[u][v] ^= 1
            A[v][u] ^= 1
        else:
            if dfs(u, v):
                print("Yes")
            else:
                print("No")


if __name__ == "__main__":
    main()
