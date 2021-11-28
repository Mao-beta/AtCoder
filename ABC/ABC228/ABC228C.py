import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()

import bisect

def main():
    N, K = NMI()
    P = [sum(NLI()) for _ in range(N)]
    SP = sorted(P)
    for p in P:
        p += 300
        idx = bisect.bisect_right(SP, p)
        x = N - idx + 1
        if x <= K:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
