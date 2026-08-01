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
    T = NI()
    for _ in range(T):
        S = SI()
        N = len(S)
        ans = ["" for _ in range(N)]
        C = Counter(S)
        CM = C.most_common()
        c, k = CM[0]
        if k > (N+1)//2:
            print("No")
        else:
            print("Yes")
            idx = 0
            for c, k in CM:
                for _ in range(k):
                    ans[idx] = c
                    idx += 2
                    if idx >= N:
                        idx -= N
                        if N % 2 == 0:
                            idx += 1
            print("".join(ans))


if __name__ == "__main__":
    main()
