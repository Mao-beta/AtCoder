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
    T = NI()
    Q = [NI() for _ in range(T)]
    G = [0] * 101

    for i in range(101):
        goto = [i-2, i-3, i-5]
        M = set()
        for j in goto:
            if j < 0: continue
            M.add(G[j])
        for g in range(10):
            if g not in M:
                G[i] = g
                break

    for n in Q:
        print("First" if G[n] else "Second")


if __name__ == "__main__":
    main()
