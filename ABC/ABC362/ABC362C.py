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
    LR = EI(N)
    lsum = 0
    rsum = 0
    ans = []
    for l, r in LR:
        lsum += l
        rsum += r
        ans.append(l)
    if lsum > 0 or rsum < 0:
        print("No")
        return
    rem = -lsum
    for i, (l, r) in enumerate(LR):
        g = r - l
        if rem >= g:
            ans[i] += g
            rem -= g
        else:
            ans[i] += rem
            rem = 0
    print("Yes")
    print(*ans)



if __name__ == "__main__":
    main()
