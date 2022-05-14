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


def main():
    N, L = NMI()
    S = [set(SI()) for _ in range(N)]
    sub = [set()]

    nums = [0] * (1<<N)
    for i in range(1, 1<<N):
        subs = None
        for k in range(N):
            if (i >> k) & 1:
                nums[i] += 1
                if subs is None:
                    subs = S[k].copy()
                else:
                    subs &= S[k]
        sub.append(subs)

    P = [pow(i, L, MOD99) for i in range(27)]
    ans = 0
    for i in range(1, 1<<N):
        num = nums[i] + 1
        ans += P[len(sub[i])] * (-1)**num
        ans %= MOD99

    print(ans)


if __name__ == "__main__":
    main()
