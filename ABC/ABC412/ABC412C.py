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
        N = NI()
        S = NLI()
        now = S[0]
        goal = S[-1]
        S.sort()
        ans = 2
        ok = True
        while now * 2 < goal:
            idx = bisect.bisect_right(S, now*2)
            t = S[idx-1]
            if t == now:
                print(-1)
                ok = False
                break
            else:
                now = t
                ans += 1
        if ok:
            print(ans)


if __name__ == "__main__":
    main()
