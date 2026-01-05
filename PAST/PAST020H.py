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
    X = []
    for i in range(N):
        l, r = NMI()
        X.append([2*l, i])
        X.append([2*r+1, i])
    X.sort()
    used = [0] * N
    stack = []
    ans = 0
    for x, i in X:
        if x % 2:
            if used[i] == 0:
                ans += 1
                while stack:
                    used[stack.pop()] = 1
        else:
            stack.append(i)
    print(ans)


if __name__ == "__main__":
    main()
