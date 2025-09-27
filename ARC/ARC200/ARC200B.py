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


def solve(A):
    if A == [1, 1, 1]:
        return True, (1, 1)
    elif A == [1, 1, 2]:
        return True, (8, 9)
    elif A[0] == A[1] == 1:
        return False, (0, 0)
    elif A[0] == 1:
        if A[1] == A[2]:
            return True, (1, 10**(A[1]-1))
        elif A[1] + 1 == A[2]:
            return True, (9, 10**(A[1]-1)*8)
        elif A[1] > A[2]:
            return False, (0, 0)
    elif A[1] == 1:
        if A[0] == A[2]:
            return True, (10**(A[0]-1), 1)
        elif A[0] + 1 == A[2]:
            return True, (10**(A[0]-1)*8, 9)
        elif A[0] > A[2]:
            return False, (0, 0)
    elif A == [2, 2, 3]:
        return True, (10, 11)

    if A[2] < max(A[0], A[1]) or A[2] > A[0] + A[1]:
        return False, (0, 0)


    # if A[2] < max(A[0], A[1]) or A[2] > A[0] + A[1] - 1:
    #     return False, (0, 0)
    if A[0] <= A[1]:
        X1 = 10 ** (A[0] - 1)
        X2 = 10 ** (A[1] - 1)
        if A[2] == A[0] + A[1]:
            X1 *= 9
            X2 *= 9
            X2 += 7
        else:
            X2 += 10 ** (A[0] + A[1] - A[2] - 1)
        return True, (X1, X2)
        # print(len(str(math.lcm(X1, X2))), A[2])
    else:
        A[0], A[1] = A[1], A[0]
        X1 = 10 ** (A[0] - 1)
        X2 = 10 ** (A[1] - 1)
        if A[2] == A[0] + A[1]:
            X1 *= 9
            X2 *= 9
            X2 += 7
        else:
            X2 += 10 ** (A[0] + A[1] - A[2] - 1)
        return True, (X2, X1)
        # print(len(str(math.lcm(X1, X2))), A[2])



def main():
    T = NI()
    for _ in range(T):
        A = NLI()
        tf, X12 = solve(A)
        if tf:
            print("Yes")
            print(*X12)
        else:
            print("No")


    # for a in range(1, 18):
    #     for b in range(1, 18):
    #         for c in range(1, 18):
    #             tf, X12 = solve([a, b, c])
    #             print("A:", a, b, c)
    #             print(tf, X12)
    #             print(X12, math.lcm(X12[0], X12[1]), len(str(math.lcm(X12[0], X12[1]))), c)
    #             if tf:
    #                 assert len(str(math.lcm(X12[0], X12[1]))) == c


if __name__ == "__main__":
    main()
