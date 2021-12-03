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
    Q = NI()
    querys = [NLI() for _ in range(Q)]
    T = []
    B = []
    for t, x in querys:
        if t == 1:
            T.append(x)
        elif t == 2:
            B.append(x)
        else:
            if x <= len(T):
                print(T[-x])
            else:
                print(B[x-1-len(T)])


if __name__ == "__main__":
    main()
