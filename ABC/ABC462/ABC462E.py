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
        A, B, X, Y = NMI()
        if X < 0:
            X *= -1
        if Y < 0:
            Y *= -1
        ans = 0
        if B >= A:
            A, B = B, A
            X, Y = Y, X
        # print(A, B, X, Y)

        if A >= B*2:
            if X >= Y:
                ans += 2*Y
                X -= Y
                if X % 2 == 0:
                    ans += X//2 * 4
                else:
                    ans += (X+1)//2 * 4 - B
            else:
                ans += 2*X
                Y -= X
                if Y % 2 == 0:
                    ans += Y//2 * 4
                else:
                    ans += (Y+1)//2 * 4 - A
        else:
            k = X+Y
            if k == 1:
                if X == 1:
                    ans = A
                else:
                    ans = B

            elif k % 2 == 0:
                ans += k//2 * (A+B)
            else:
                ans += (k-1)//2 * (A+B) + min(A, B)
        print(ans)


if __name__ == "__main__":
    main()
