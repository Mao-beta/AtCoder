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

# アルファベットと数字の対応
alp_to_num = {chr(i+97): i for i in range(26)}
ALP_to_num = {chr(i+97).upper(): i for i in range(26)}
num_to_alp = {i: chr(i+97) for i in range(26)}
num_to_ALP = {i: chr(i+97).upper() for i in range(26)}


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    N = NI()
    ans = []

    def dfs(s, i, max_num):
        if i == N:
            ans.append(s)
            return

        for n in range(max_num+2):
            dfs(s + num_to_alp[n], i+1, max(max_num, n))

    dfs("a", 1, 0)
    ans.sort()
    for a in ans:
        print(a)


if __name__ == "__main__":
    main()