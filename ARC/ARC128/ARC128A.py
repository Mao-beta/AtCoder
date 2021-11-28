import sys
import math
from collections import deque

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
    ans = [0] * N
    now = -1
    phase = 0
    for i in range(N-1):
        a, b = A[i], A[i+1]
        if phase == 0:
            if a > b:
                ans[i] = 1
                phase = 1

        else:
            if a <= b:
                ans[i] = 1
                phase = 0

    if phase == 1:
        if A[-1] < A[-2]:
            ans[-1] = 1
        else:
            idx = 0
            for i in range(N):
                if ans[i] == 1:
                    idx = max(idx, i)
            ans[idx] = 0

    print(*ans)


if __name__ == "__main__":
    main()
