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
    A = [0] + NLI()

    seen = set()

    def dfs(now):
        v = A[now]

        if v in seen_now:
            v_idx = D.index(v)
            ans = D[v_idx:]
            print(len(ans))
            print(*ans)
            exit()

        D.append(v)
        seen_now.add(v)
        dfs(v)
        seen_now.discard(v)
        D.pop()

    for s in range(1, N+1):
        if s in seen:
            continue
        D = [s]
        seen_now = {s}
        dfs(s)


if __name__ == "__main__":
    main()
