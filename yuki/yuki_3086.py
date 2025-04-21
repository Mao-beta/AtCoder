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
    N = NI()
    AB = EI(N)
    D = []
    ans = [0] * N
    now = 0
    for i, (a, b) in enumerate(AB, start=1):
        if a == 1 or b == 2:
            D.append([i, a, b])
        elif b == 1:
            ans[now] = i
            now += 1
            while D and (D[-1][1] == 1 or D[-1][2] == 2):
                x, y, z = D.pop()
                ans[now] = x
                now += 1
        else:
            ans[now] = i
            now += 1
            while D and D[-1][1] == 1:
                ans[now] = D.pop()[0]
                now += 1
    while D:
        ans[now] = D.pop()[0]
        now += 1
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
