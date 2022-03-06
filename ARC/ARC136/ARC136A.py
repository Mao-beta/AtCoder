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


def main():
    N = NI()
    S = SI()
    SC = S.split("C")
    ans = []
    for ss in SC:
        C = Counter(ss)
        B = C["A"] * 2 + C["B"]
        A = B // 2
        B %= 2
        s = "A" * A + "B" * B
        ans.append(s)

    print("C".join(ans))


if __name__ == "__main__":
    main()
