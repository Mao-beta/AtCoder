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
    N, K, C = NMI()
    S = SI()

    if S.count("o") == K:
        for i in range(N):
            if S[i] == "o":
                print(i+1)
        return

    if C == 0:
        return

    A = set()
    B = set()
    cnt = C
    for i in range(N):
        if S[i] == "o" and cnt >= C:
            cnt = 0
            A.add(i+1)
        else:
            cnt += 1

    cnt = C
    for i in range(N-1, -1, -1):
        if S[i] == "o" and cnt >= C:
            cnt = 0
            B.add(i + 1)
        else:
            cnt += 1

    ans = sorted(list(A & B))
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
