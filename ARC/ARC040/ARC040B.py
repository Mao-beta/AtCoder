import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
    N, R = NMI()
    S = list(SI())
    if "." not in S:
        print(0)
        return
    M = max("".join(S).rindex(".") - R + 1, 0)
    ans = M
    for i in range(N):
        if i == M:
            ans += 1
            break

        if S[i] == "o":
            continue
        else:
            ans += 1
            for j in range(i, i+R):
                if j >= N:
                    break
                S[j] = "o"
    print(ans)


if __name__ == "__main__":
    main()
