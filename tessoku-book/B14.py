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


# 半分全列挙
def split_and_list(A):
    """
    半分全列挙
    :param A: 長さ40以下くらいのList
    :return: 前半と後半それぞれについて、各部分集合の和のList
    """

    def solve_half(A_half):
        n = len(A_half)
        res = []
        for case in range(1<<n):
            now = 0
            for i in range(n):
                if (case >> i) & 1:
                    now += A_half[i]
            res.append(now)
        res.sort()
        return res

    N = len(A)
    return solve_half(A[:N//2]), solve_half(A[N//2:])


def main():
    N, K = NMI()
    A = NLI()
    X, Y = split_and_list(A)
    Y = set(Y)
    for x in X:
        if K - x in Y:
            print("Yes")
            exit()
    print("No")


if __name__ == "__main__":
    main()
