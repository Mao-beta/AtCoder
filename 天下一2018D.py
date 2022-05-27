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
    now = 1
    ans = [[1], [1]]

    while True:
        if N == now:
            print("Yes")
            print(len(ans))
            for S in ans:
                print(len(S), *S)
            exit()

        if now > N:
            print("No")
            exit()

        s = len(ans)
        ans.append([])
        for i in range(s):
            x = now + i + 1
            ans[i].append(x)
            ans[-1].append(x)
        now += s


if __name__ == "__main__":
    main()
