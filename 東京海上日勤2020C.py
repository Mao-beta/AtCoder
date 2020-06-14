import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, K = NMI()
    A = NLI()

    for k in range(min(K, 42)):
        tmp = [0] * (N+1)
        for i, a in enumerate(A):
            tmp[max(0, i-a)] += 1
            tmp[min(N, i+a+1)] -= 1
        cum = [0] * (N+1)
        for i, t in enumerate(tmp):
            if i == 0:
                cum[0] = t
                continue
            cum[i] = cum[i-1] + t
        A = cum[:-1]
    print(" ".join(map(str, A)))


if __name__ == "__main__":
    main()