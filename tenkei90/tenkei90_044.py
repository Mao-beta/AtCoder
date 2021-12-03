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
    N, Q = NMI()
    A = NLI()
    querys = [NLI() for _ in range(Q)]
    rshift = 0

    for t, x, y in querys:
        x = (x - 1 - rshift) % N
        y = (y - 1 - rshift) % N

        if t == 1:
            A[x], A[y] = A[y], A[x]
        elif t == 2:
            rshift += 1
            rshift %= N
        else:
            print(A[x])


if __name__ == "__main__":
    main()
