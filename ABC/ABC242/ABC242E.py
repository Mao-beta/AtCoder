import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

if "PyPy" in sys.version:
    import pypyjit

    pypyjit.set_param('max_unroll_recursion=-1')

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

ALP_to_num = {chr(i+97).upper(): i for i in range(26)}
num_to_ALP = {i: chr(i+97).upper() for i in range(26)}

def main():
    T = NI()
    for _ in range(T):
        N = NI()
        S = SI()
        R = S[::-1]
        SR = S[:(N+1)//2] + R[(N+1)//2:]

        flag = False
        if SR > S:
            flag = True
        S = [ALP_to_num[s] for s in S[:(N+1)//2]][::-1]

        ans = 0 if flag else 1
        p = 1
        for s in S:
            ans += s * p
            p = p * 26 % MOD99
            ans %= MOD99

        print(ans)


if __name__ == "__main__":
    main()
