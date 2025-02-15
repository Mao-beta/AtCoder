import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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
    N, B = NMI()
    A = NLI()
    S = set()
    for a in A:
        if a in S:
            rem = N - len(S)
        else:
            rem = N - len(S) - 1
        # 今までのどれか1つ以上が偽
        ans = pow(2, len(S), B) - 1
        # aが新しい場合は自由
        if a not in S:
            ans *= 2
        # 全部真
        ans += 1
        # のこり
        ans *= pow(2, rem, B)
        ans %= B
        print(ans)
        S.add(a)


if __name__ == "__main__":
    main()
