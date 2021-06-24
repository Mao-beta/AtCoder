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
    N, M = NMI()
    P = [NLI() for _ in range(M)]
    P.sort()
    S = {N}
    prev_x = -1
    T_in = set()
    T_out = set()

    for x, y in P:
        if x != prev_x:
            S -= T_out
            S |= T_in
            T_in.clear()
            T_out.clear()
            prev_x = x

        if y in S:
            T_out.add(y)
        if y-1 in S or y+1 in S:
            T_in.add(y)

    S = (S - T_out) | T_in

    print(len(S))



if __name__ == "__main__":
    main()
