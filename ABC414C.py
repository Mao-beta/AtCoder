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


def convert_base(str_n, base0, base1):
    """
    base0進数の文字列str_nを、base1進数の文字列に変換する
    """
    tmp = int(str_n)

    res = []
    while tmp > 0:
        m = tmp % base1
        res.append(m)
        tmp //= base1
    return res == res[::-1]


def main():
    A = NI()
    N = NI()

    S = set()
    for i in range(1, 10**6):
        i = str(i)
        X = i + i[:-1][::-1]
        Y = convert_base(X, 10, A)
        if int(X) <= N and Y:
            S.add(int(X))
        X = i + i[::-1]
        Y = convert_base(X, 10, A)
        if int(X) <= N and Y:
            S.add(int(X))
    print(sum(S))


if __name__ == "__main__":
    main()
