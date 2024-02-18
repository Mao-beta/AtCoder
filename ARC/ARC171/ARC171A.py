import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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


def solve(N, A, B):
    if A > N:
        return False
    if A == N and B > 0:
        return False
    
    half = (N+1) // 2
    col = N - A

    if A <= N//2:
        row = A + (N-2*A+1)//2
        if B <= row * col:
            return True
        else:
            return False

    if A <= half:
        row = A + (N-2*A)//2
        if B <= row * col:
            return True
        else:
            return False
    else:
        row = N - A
        if B <= row * col:
            return True
        else:
            return False


def test():
    for N in range(4):
        for AB in range(1, N**2+1):
            for A in range(7):
                B = AB - A
                if B < 0:
                    continue
                print(N, A, B)
                if solve(N, A, B):
                    print("Yes")
                else:
                    print("No")


def main():
    T = NI()
    for _ in range(T):
        N, A, B = NMI()
        if solve(N, A, B):
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
