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
    N, T = NMI()
    S = SI()
    X = NLI()
    ans = 0
    M = [X[i] for i in range(N) if S[i] == "0"]
    P = [X[i] for i in range(N) if S[i] == "1"]
    M.sort()
    P.sort()
    for p in P:
        l = bisect.bisect_left(M, p)
        r = bisect.bisect_right(M, p+2*T)
        ans += r-l
    print(ans)



if __name__ == "__main__":
    main()
