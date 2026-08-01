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
    S = SI()
    T = SI()
    N = len(S)
    M = len(T)
    C2I = [[] for _ in range(26)]
    for i, s in enumerate(S):
        s = ord(s) - ord("a")
        C2I[s].append(i)
    for s in range(26):
        C2I[s].append(N)
    ans = 0
    for l in range(N):
        r = l
        for j, t in enumerate(T):
            t = ord(t) - ord("a")
            idx = bisect.bisect_left(C2I[t], r)
            if idx == len(C2I[t]):
                r = N
                break
            # print(l, j, t, idx, len(C2I[t]))
            r = C2I[t][idx] + 1
            if r == N:
                if j == M-1:
                    r -= 1
                    break
                else:
                    break
            if j == M-1:
                r -= 1
        # print(l, r)
        ans += r-l
    print(ans)


if __name__ == "__main__":
    main()
