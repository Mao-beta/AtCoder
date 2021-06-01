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
    N = NI()
    W = NLI()
    B = NLI()

    G = [[0]*1326 for _ in range(51)]
    for w in range(51):
        for b in range(1326):
            X = set()
            if w > 0 and b+w < 1326:
                X.add(G[w-1][b+w])
            for k in range(b-b//2, b):
                X.add(G[w][k])
            for g in range(1500):
                if g not in X:
                    G[w][b] = g
                    break

    ans = 0
    for w, b in zip(W, B):
        ans ^= G[w][b]
    print("Second" if ans == 0 else "First")



if __name__ == "__main__":
    main()
