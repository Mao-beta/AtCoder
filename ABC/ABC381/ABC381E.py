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
    N, Q = NMI()
    S = SI()
    ONE = [0] * (N+1) # S[:i]の1
    TWO = [0] * (N+1) # S[i:]の2
    SLA = []
    for i, s in enumerate(S):
        if s == "1":
            ONE[i+1] = ONE[i] + 1
        else:
            ONE[i+1] = ONE[i]
        if s == "/":
            SLA.append(i)
    for i in range(N-1, -1, -1):
        s = S[i]
        if s == "2":
            TWO[i] = TWO[i+1] + 1
        else:
            TWO[i] = TWO[i+1]

    # print(ONE)
    # print(TWO)
    # print(SLA)
    for _ in range(Q):
        l, r = NMI()
        l -= 1
        li = bisect.bisect_left(SLA, l)
        ri = bisect.bisect_left(SLA, r)
        # print(l, r, li, ri)
        bl = li
        br = ri
        while br - bl > 1:
            mid = (bl + br) // 2
            s = SLA[mid]
            one = ONE[s] - ONE[l]
            two = TWO[s] - TWO[r]
            if one == two:
                bl = mid
                br = mid + 1
            elif one > two:
                br = mid
            else:
                bl = mid
        # print(bl, br)
        if bl == br:
            print(0)
            continue
        one = ONE[SLA[bl]] - ONE[l]
        two = TWO[SLA[bl]] - TWO[r]
        ans = min(one, two) * 2 + 1

        if br < ri:
            one = ONE[SLA[br]] - ONE[l]
            two = TWO[SLA[br]] - TWO[r]
            ans = max(ans, min(one, two) * 2 + 1)

        print(ans)


if __name__ == "__main__":
    main()
