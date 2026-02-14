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
    XY = EI(N)
    G = [defaultdict(lambda: -1) for _ in range(N+1)]
    sames = [[] for _ in range(N+1)]
    rev = list(range(N+1))
    for i, (x, y) in enumerate(XY, start=1):
        x = rev[x]
        if G[x][y] == -1:
            G[x][y] = i
        else:
            sames[G[x][y]].append(i)
            rev[i] = G[x][y]
    # print(G)
    stack = deque()
    stack.append(0)
    ans = []
    while stack:
        now = stack.pop()
        ans.append(now)
        for same in sames[now]:
            ans.append(same)
        for key, val in sorted(G[now].items(), reverse=True):
            stack.append(val)
            # print(f"stack append {val}, {stack=}")
    print(*ans[1:])


if __name__ == "__main__":
    main()
