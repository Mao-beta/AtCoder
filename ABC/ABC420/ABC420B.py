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
    N, M = NMI()
    S = [SI() for _ in range(N)]
    C = [0] * N
    for j in range(M):
        one = 0
        zero = 0
        for i in range(N):
            if S[i][j] == "1":
                one += 1
            else:
                zero += 1
        if one < zero:
            for i in range(N):
                if S[i][j] == "1":
                    C[i] += 1
        else:
            for i in range(N):
                if S[i][j] == "0":
                    C[i] += 1
    m = max(C)
    ans = [i+1 for i in range(N) if C[i] == m]
    print(*ans)


if __name__ == "__main__":
    main()
