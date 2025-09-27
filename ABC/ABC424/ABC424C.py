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
    AB = EI(N)
    G = [[] for _ in range(N)]
    que = deque()
    for i, (a, b) in enumerate(AB):
        if a == b == 0:
            que.append(i)
        else:
            a, b = a-1, b-1
            G[a].append(i)
            G[b].append(i)
    seen = [0] * N
    while que:
        i = que.popleft()
        if seen[i]:
            continue
        seen[i] = 1
        for j in G[i]:
            if not seen[j]:
                que.append(j)
    print(sum(seen))


if __name__ == "__main__":
    main()
