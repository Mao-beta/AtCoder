import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

if "PyPy" in sys.version:
    import pypyjit

    pypyjit.set_param('max_unroll_recursion=-1')

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
    a, b, c = SMI()
    ta, tb, tc = SMI()

    D = {a: "R", b: "G", c: "B"}
    ta, tb, tc = D[ta], D[tb], D[tc]

    if ta == "R" and tb == "G" and tc == "B":
        print("Yes")
    elif ta == "R" and tb == "B" and tc == "G":
        print("No")
    elif ta == "G" and tb == "R" and tc == "B":
        print("No")
    elif ta == "G" and tb == "B" and tc == "R":
        print("Yes")
    elif ta == "B" and tb == "R" and tc == "G":
        print("Yes")
    elif ta == "B" and tb == "G" and tc == "R":
        print("No")


if __name__ == "__main__":
    main()
