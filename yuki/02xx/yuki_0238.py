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
    S = list(SI())
    N = len(S)
    if S == S[::-1]:
        S.insert(N//2, S[N//2])
        print("".join(S))
        return

    l = 0
    r = N-1
    ans = []
    while l < r:
        if S[l] == S[r]:
            l += 1
            r -= 1
        else:
            ans.append([l, r])
            l += 1

    if len(ans) == 1:
        l, r = ans[0]
        S.insert(r+1, S[l])
        print("".join(S))
        return

    l = 0
    r = N-1
    ans = []
    while l < r:
        if S[l] == S[r]:
            l += 1
            r -= 1
        else:
            ans.append([l, r])
            r -= 1

    if len(ans) == 1:
        l, r = ans[0]
        S.insert(l, S[r])
        print("".join(S))
        return

    print("NA")


if __name__ == "__main__":
    main()
