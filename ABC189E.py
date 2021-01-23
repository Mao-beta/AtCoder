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


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    N = NI()
    P = [NLI() for _ in range(N)]
    M = NI()
    ops = [SI() for _ in range(M)]
    Q = NI()
    querys = [NLI() for _ in range(Q)]

    cum = []

    a, b, c, d = 1, 0, 1, 0
    rev = False
    cum.append([a, b, c, d, rev])
    for op in ops:
        if rev:
            if op == "1": op = "2"
            elif op == "2": op = "1"
            elif op[0] == "3":
                op = "4" + op[1:]
            else:
                op = "3" + op[1:]

        if op == "1":
            rev = not rev
            a, b = -a, -b
        elif op == "2":
            rev = not rev
            c, d = -c, -d
        elif op[0] == "3":
            _, p = map(int, op.split())
            a, b = -a, 2*p - b
        elif op[0] == "4":
            _, p = map(int, op.split())
            c, d = -c, 2*p - d
        else:
            print("error")
        cum.append([a, b, c, d, rev])

    for query in querys:
        qa, qb = query
        a, b, c, d, rev = cum[qa]
        x, y = P[qb-1]
        #print(a, b, c, d, rev, x, y)

        if not rev:
            print(a*x+b, c*y+d)
        else:
            print(c*y+d, a*x+b)


if __name__ == "__main__":
    main()
