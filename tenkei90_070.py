import sys
import math
from collections import defaultdict
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
    X = []
    Y = []
    for _ in range(N):
        x, y = NMI()
        X.append(x)
        Y.append(y)
    X.sort()
    Y.sort()
    mx = X[N//2]
    my = Y[N//2]
    ans = 0
    for x, y in zip(X, Y):
        ans += abs(mx - x) + abs(my - y)
    print(ans)


if __name__ == "__main__":
    main()
