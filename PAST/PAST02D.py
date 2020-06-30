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
    ans = set()
    N = len(S)
    ans.add(".")
    for i in range(N):
        ans.add(S[i])

    if N == 1:
        print(len(ans))
        exit()

    ans.add("..")
    for i in range(N-1):
        ans.add("." + S[i+1])
        ans.add(S[i] + ".")
        ans.add(S[i:i+2])

    if N == 2:
        print(len(ans))
        exit()

    ans.add("...")
    for i in range(N-2):
        ans.add("." + S[i+1] + ".")
        ans.add(S[i] + "..")
        ans.add(".." + S[i+2])
        ans.add(S[i:i+2] + ".")
        ans.add(S[i] + "." + S[i+2])
        ans.add("." + S[i+1:i+3])
        ans.add(S[i:i+3])

    print(len(ans))


if __name__ == "__main__":
    main()