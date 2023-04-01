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


def main():
    N = NI()
    S = SI()
    T = SI()

    sn = S.count("1")
    tn = T.count("1")
    if sn < tn or (sn - tn) % 2:
        print(-1)
        return

    targets = deque()
    ans = 0
    for i, (s, t) in enumerate(zip(S, T)):
        s, t = int(s), int(t)
        if t:
            targets.append(i)

        if s:
            if targets:
                x = targets.popleft()
                ans += i - x
            else:
                targets.append(i)

    if targets:
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    main()
