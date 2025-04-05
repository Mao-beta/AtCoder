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
    S = SI()
    ans = []
    x = 0
    out = False
    l = 0
    while x < N:
        if out:
            if S[x:x+2] == r"*/":
                out = False
                for _ in range(x-l):
                    ans.pop()
                x += 2
            else:
                ans.append(S[x])
                x += 1
        else:
            if S[x:x+2] == r"/*":
                out = True
                l = x
                ans.append(S[x])
                ans.append(S[x+1])
                x += 2
            else:
                ans.append(S[x])
                x += 1
    print("".join(ans))


if __name__ == "__main__":
    main()
