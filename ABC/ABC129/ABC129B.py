import sys
import math
from collections import deque
import bisect

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    W = NLI()
    cum = []
    cum.append(W[0])
    for i in range(1, N):
        cum.append(cum[-1] + W[i])
    total = cum[-1]
    idx = 0
    for i in range(N):
        if cum[i] <= total / 2:
            idx = i
        else:
            idx_r = i
            break
    print(min(abs(total - cum[idx]*2) ,abs(total - cum[idx_r]*2)))




if __name__ == "__main__":
    main()