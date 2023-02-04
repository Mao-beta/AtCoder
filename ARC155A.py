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


def print_err(*args):
    print(*args, file=sys.stderr)


def parindrome(s):
    return s == s[::-1]


def solve(N, K, S):
    X = K // N
    r = K % N
    # print(S + S[:r][::-1])
    if parindrome(S + S[:r][::-1]) and parindrome(S[:r][::-1] + S):
        return True
    else:
        return False


def main():
    T = NI()
    for _ in range(T):
        N, K = NMI()
        S = SI()
        if solve(N, K, S):
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
