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
    K = NI()
    A, B = SMI()

    def convert_base(str_n, base0, base1):
        """
        base0進数の文字列str_nを、base1進数の文字列に変換する
        """
        tmp = 0
        for i, n in enumerate(str_n[::-1]):
            tmp += pow(base0, i) * int(n)

        res = ""
        while tmp > 0:
            m = tmp % base1
            res = str(m) + res
            tmp //= base1
        return res or "0"

    A = convert_base(A, K, 10)
    B = convert_base(B, K, 10)
    print(int(A) * int(B))


if __name__ == "__main__":
    main()
