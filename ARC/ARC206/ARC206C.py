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
    N = NI()
    A = NLI()
    A = [x-1 if x >= 1 else -1 for x in A]

    r_max = -1
    l_min = N
    out_idx = -1
    out_val = -1
    each_idx = -1
    for i in range(N):
        a = A[i]
        if a == -1:
            continue
        # print(i, a)
        if abs(a-i) != 1:
            if out_idx != -1:
                print(0)
                return
            out_idx = i
            out_val = a

        if i > 0 and a == i-1:
            l_min = min(l_min, i)
        if i < N-1 and a == i+1:
            r_max = max(r_max, i)

        if i < N-1 and A[i] == i+1 and A[i+1] == i:
            if each_idx >= 0:
                print(0)
                return
            each_idx = i

    # print("&")

    if each_idx >= 0 and out_idx >= 0:
        print(0)
        return

    # outが自己
    if out_idx != -1 and out_val == out_idx:
        for i in range(N):
            if i < out_idx:
                j = i+1
            elif i > out_idx:
                j = i-1
            else:
                j = i
            if A[i] != -1 and A[i] != j:
                print(0)
                return
        print(1)
        return

    # print("$")

    # outが自己以外
    if out_idx != -1 and out_val != out_idx:
        for i in range(N):
            if i < min(out_idx, out_val):
                j = i+1
            elif i > min(out_idx, out_val):
                j = i-1
            elif i != out_idx:
                if out_idx < out_val:
                    j = i-1
                else:
                    j = i+1
            if A[i] != -1 and A[i] != j:
                print(0)
                return
        print(1)
        return

    # eachあり
    if each_idx >= 0:
        for i in range(N):
            if i <= each_idx:
                j = i + 1
            else:
                j = i - 1
            if A[i] != -1 and A[i] != j:
                print(0)
                return
        print(1)
        return

    # out=0 and each=0
    # print("#", r_max, l_min, l_min - r_max - 1)

    if r_max > l_min:
        print(0)
        return

    x = l_min - r_max - 1
    if x == 0:
        print(1)
        return
    # RRRRRXXXXXLLLL
    ans = N * x - (x-1)
    print(ans % MOD99)


if __name__ == "__main__":
    main()
