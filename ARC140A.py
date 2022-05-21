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

alp_to_num = {chr(i+97): i for i in range(26)}

# 約数列挙（単体）
def divisors(x):
    res = set()
    for i in range(1, int(x**0.5) + 2):
        if x % i == 0:
            res.add(i)
            res.add(x//i)
    return res


def main():
    N, K = NMI()
    S = SI()
    S = [alp_to_num[s] for s in S]

    D = sorted(list(divisors(N)))

    for d in D:
        tmp = 0
        for start in range(d):
            C = Counter(S[start::d])
            x = C.most_common(1)[0][1]
            tmp += N // d - x

        if tmp > K:
            continue
        print(d)
        exit()


if __name__ == "__main__":
    main()
