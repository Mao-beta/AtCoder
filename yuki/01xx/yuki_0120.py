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
    T = NI()
    for _ in range(T):
        N = NI()
        A = NLI()
        C = Counter(A)
        if len(C) < 3:
            print(0)
            continue
        MC = C.most_common()
        x, y = MC[0][1], MC[1][1]
        rem = N - x - y
        if rem <= y:
            print(rem)
        else:
            ans = y
            x -= y
            rem -= y
            if rem >= x*2:
                ans += x
                rem -= x*2
                ans += rem // 3
                print(ans)
            else:
                ans += rem // 2
                print(ans)


if __name__ == "__main__":
    main()
