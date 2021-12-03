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


def main():
    N = NI()
    S = SI()
    l = 0
    r = 0
    cnt_ox = [0, 0]
    ans = 0
    while l < N-1:
        while r < N and (cnt_ox[0] == 0 or cnt_ox[1] == 0):
            s = S[r]
            if s == "o":
                cnt_ox[0] += 1
            else:
                cnt_ox[1] += 1
            r += 1

        if not(cnt_ox[0] == 0 or cnt_ox[1] == 0):
            ans += N - r + 1
        s = S[l]
        if s == "o":
            cnt_ox[0] -= 1
        else:
            cnt_ox[1] -= 1
        l += 1

    print(ans)


if __name__ == "__main__":
    main()
