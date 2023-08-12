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
    A = []
    for i in range(N):
        C = NI()
        S = set(NMI())
        A.append([len(S), i+1, S])
    X = NI()
    A = [[l, idx] for l, idx, s in A if X in s]
    if len(A) == 0:
        print(0)
        return

    A.sort()
    m = A[0][0]
    ans = [idx for l, idx in A if l == m]
    ans.sort()
    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    main()
