import sys
import math
from collections import Counter
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    S = SI()
    C = Counter(S)
    T = NI()

    x = abs(C["L"] - C["R"])
    y = abs(C["U"] - C["D"])
    Q = C["?"]
    if T == 1:
        print(x+y+Q)
    else:
        if x+y >= Q:
            print(x+y-Q)
        else:
            Q -= x+y
            print(Q%2)


if __name__ == "__main__":
    main()
