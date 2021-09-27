import sys
import math
from collections import deque
import bisect
from itertools import accumulate

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    A = NLI()
    X = NI()
    AA = [0] + A + A
    C = list(accumulate(AA))
    S = sum(A)
    base = X // S * N
    X %= S
    idx = bisect.bisect_left(C, X+1)
    print(base + idx)


if __name__ == "__main__":
    main()
