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


def main():
    N, C = NMI()
    X = []
    Y = []
    for _ in range(N):
        x, y = NMI()
        X.append(x)
        Y.append(y)
    p = sum(X) / N
    ans = 0
    for x, y in zip(X, Y):
        ans += (p-x)**2 + (C-y)**2
    print(ans)


if __name__ == "__main__":
    main()
