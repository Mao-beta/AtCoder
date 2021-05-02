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
    T = SI()
    if T == "0" or T == "11" or T == "10" or T == "110":
        print(10**10)
        exit()
    if T == "1":
        print(10 ** 10 * 2)
        exit()
    if T == "01" or T == "101" or T == "011":
        print(10**10 - 1)
        exit()

    T_0 = T[0::3]
    T_1 = T[1::3]
    T_2 = T[2::3]

    if (set(T_0) == set("1") and set(T_1) == set("1") and set(T_2) == set("0")):
        if N % 3 == 0:
            print(10**10 - (N//3) + 1)
        else:
            print(10 ** 10 - (N // 3))
    elif (set(T_0) == set("1") and set(T_1) == set("0") and set(T_2) == set("1")):
        if N % 3 == 2:
            print(10**10 - ((N-2)//3))
        else:
            print(10**10 - ((N-2)//3) - 1)
    elif (set(T_0) == set("0") and set(T_1) == set("1") and set(T_2) == set("1")):
        if N % 3 == 1:
            print(10**10 - ((N-1)//3))
        else:
            print(10**10 - ((N-1)//3) - 1)

    else:
        print(0)



if __name__ == "__main__":
    main()
