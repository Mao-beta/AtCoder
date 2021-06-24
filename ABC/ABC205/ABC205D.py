import sys
import math
from collections import deque
from itertools import accumulate
import bisect

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, Q = NMI()
    A = [0] + NLI()
    querys = [NI() for _ in range(Q)]

    B = [0] + [A[i+1] - A[i] - 1 for i in range(N)]
    C = list(accumulate(B)) + [10**20]

    for k in querys:
        idx = bisect.bisect_left(C, k)
        print(A[idx-1] + k - C[idx-1])



if __name__ == "__main__":
    main()
