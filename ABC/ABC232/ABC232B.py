import sys
import math
from collections import deque

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


# アルファベットと数字の対応
alp_to_num = {chr(i+97): i for i in range(26)}
ALP_to_num = {chr(i+97).upper(): i for i in range(26)}
num_to_alp = {i: chr(i+97) for i in range(26)}
num_to_ALP = {i: chr(i+97).upper() for i in range(26)}


def main():
    S = [alp_to_num[s] for s in SI()]
    T = [alp_to_num[s] for s in SI()]

    for i in range(26):
        SS = [(s+i)%26 for s in S]
        if SS == T:
            print("Yes")
            exit()

    print("No")



if __name__ == "__main__":
    main()
