import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict
from functools import lru_cache

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
    # input
    X = SI()
    ans = []
    C = [0]
    for x in X:
        C.append(C[-1] + int(x))

    res = 0
    for i, c in enumerate(C[::-1]):
        ans.append((c + res) % 10)
        res = (c + res) // 10

    ans.append(res)
    ans = ans[::-1]
    ans = "".join(map(str, ans))
    lz = True
    for a in ans:
        if lz and a == "0":
            continue
        else:
            print(a, end="")
            lz = False
    print()


if __name__ == "__main__":
    main()
