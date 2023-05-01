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
    N, L, K = NMI()
    S = [SI() for _ in range(N)]
    ans = 0
    for C in combinations(range(L), L-K):
        tmp = Counter()
        for SS in S:
            X = [SS[c] for c in C]
            tmp["".join(X)] += 1

        ans = max(ans, tmp.most_common(1)[0][1])

    print(ans)


if __name__ == "__main__":
    main()
