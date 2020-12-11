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
    S = SI()
    if len(S) <= 2:
        if int(S) in [8, 16, 61, 24, 42, 32, 23, 40, 48, 84, 56, 65, 64, 46, 72, 27, 80, 88, 96, 69]:
            print("Yes")
            exit()
        elif len(S) <= 2:
            print("No")
            exit()

    E = [str(i*8).zfill(3) for i in range(125)]
    D = {i:0 for i in range(10)}
    for s in S:
        D[int(s)] += 1
    for e in E:
        F = {i:0 for i in range(10)}
        for ee in e:
            F[int(ee)] += 1
        is_ok = True
        for num, n in list(F.items()):
            if n > D[num]:
                is_ok = False
        if is_ok:
            print("Yes")
            exit()
    print("No")





if __name__ == "__main__":
    main()
