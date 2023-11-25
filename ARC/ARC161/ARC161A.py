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
    A = NLI()
    A.sort(reverse=True)
    ans = [0] * N
    for i, a in enumerate(A):
        if i < N // 2:
            ans[i*2+1] = a
        else:
            ans[(i-N//2)*2] = a

    for i in range(1, N, 2):
        if ans[i-1] < ans[i] and ans[i] > ans[i+1]:
            continue
        print("No")
        exit()

    print("Yes")


if __name__ == "__main__":
    main()
