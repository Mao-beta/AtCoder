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
    H, W = NMI()
    A = EI(H)
    B = EI(H)
    mx = 80
    base = mx * (H+W-1)
    dp = [0 for _ in range(H*W)]
    dp[0] |= 1 << (base+A[0][0]-B[0][0])
    dp[0] |= 1 << (base-A[0][0]+B[0][0])
    for hw in range(H*W):
        h, w = divmod(hw, W)
        dh, dw = 0, 1
        nh, nw = h + dh, w + dw
        if 0 <= nh < H and 0 <= nw < W:
            x = abs(A[nh][nw] - B[nh][nw])
            dp[nh * W + nw] |= dp[hw] << x
            dp[nh * W + nw] |= dp[hw] >> x
        dh, dw = 1, 0
        nh, nw = h + dh, w + dw
        if 0 <= nh < H and 0 <= nw < W:
            x = abs(A[nh][nw] - B[nh][nw])
            dp[nh * W + nw] |= dp[hw] << x
            dp[nh * W + nw] |= dp[hw] >> x
    ans = 10**15
    d = dp[-1]
    for m in range(base*2+1):
        if d & 1:
            a = abs(m - base)
            if a < ans:
                ans = a
        d >>= 1
    print(ans)


if __name__ == "__main__":
    main()
