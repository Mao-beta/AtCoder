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
    N = NI()
    AB = EI(N)
    ans = [0] * (N+1)
    in_events = defaultdict(int)
    out_events = defaultdict(int)
    for a, b in AB:
        in_events[a] += 1
        out_events[a+b] += 1

    keys = sorted(list(set(in_events.keys() | out_events.keys())))

    now = 0
    prev = 0
    for key in keys:
        ans[now] += key - prev
        now -= out_events[key]
        now += in_events[key]
        prev = key

    print(*ans[1:])


if __name__ == "__main__":
    main()
