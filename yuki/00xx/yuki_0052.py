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
    S = deque(SI())
    N = len(S)
    ans = set()
    for case in range(1<<N):
        T = S.copy()
        res = []
        for i in range(N):
            if (case >> i) & 1:
                res.append(T.pop())
            else:
                res.append(T.popleft())
        ans.add("".join(res))
    print(len(ans))


if __name__ == "__main__":
    main()
