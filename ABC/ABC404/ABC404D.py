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
    tmp = 0
    for i, n in enumerate(str_n[::-1]):
        tmp += pow(base0, i) * int(n)

    res = ""
    while tmp > 0:
        m = tmp % base1
        res = str(m) + res
        tmp //= base1
    return res or "0"


def main():
    N, M = NMI()
    C = NLI()
    Z = [[] for _ in range(N)]
    for a in range(M):
        k, *z = NMI()
        for zz in z:
            Z[zz-1].append(a)
    ans = 10**18
    for i in range(3**N):
        t = convert_base(str(i), 10, 3).zfill(N)
        K = [0] * M
        c = 0
        for z in range(N):
            c += int(t[z]) * C[z]
            for j in Z[z]:
                K[j] += int(t[z])
        if min(K) >= 2:
            ans = min(ans, c)
    print(ans)


if __name__ == "__main__":
    main()
