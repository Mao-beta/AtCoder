import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

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


def solve(N):
    if N < 7:
        return -1

    N = list(bin(N)[2:])
    # print(N)

    if N.count("1") >= 3:
        ans = []
        cnt = 0
        for s in N:
            if cnt < 3 and s == "1":
                ans.append(s)
                cnt += 1
            else:
                ans.append("0")
    elif N.count("1") == 1:
        k = len(N) - 1
        ans = ["111"] + ["0"] * (k-3)
    else:
        idx = "".join(N).rindex("1")
        # print(idx)
        if idx >= len(N) - 2:
            k = len(N) - 1
            ans = ["111"] + ["0"] * (k - 3)
        else:
            ans = ["1"] + ["0"] * idx + ["11"] + ["0"] * (len(N)-(idx+3))

    ans = "".join(ans)
    # print(ans)
    ans = int(ans, 2)

    return ans


def main():
    T = NI()
    for _ in range(T):
        N = NI()
        ans = solve(N)
        print(ans)


if __name__ == "__main__":
    main()
