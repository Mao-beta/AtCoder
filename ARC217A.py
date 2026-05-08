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
    T = NI()
    for _ in range(T):
        N = NI()
        if N % 2:
            ans = [i for i in range(N, 0, -1)]
            for i in range(0, N, 4):
                if i < N and i+1 < N:
                    ans[i], ans[i+1] = ans[i+1], ans[i]
            print(*ans)
        else:
            ans = [i for i in range(N-1, 0, -1)]
            for i in range(0, N-1, 4):
                if i < N-1 and i + 1 < N-1:
                    ans[i], ans[i + 1] = ans[i + 1], ans[i]
            ans.append(N)
            print(*ans)


if __name__ == "__main__":
    main()
