import sys
import math
from collections import deque
from itertools import product

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    S = input()
    for op1, op2, op3 in product("+-", repeat=3):
        q = S[0]+op1+S[1]+op2+S[2]+op3+S[3]
        if eval(q) == 7:
            print(q + "=7")
            exit()


if __name__ == "__main__":
    main()