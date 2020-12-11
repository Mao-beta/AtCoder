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
    T = SI()
    ls, lt = len(S), len(T)
    ans = 1100
    for i in range(ls-lt+1):
        tmp = 0
        tS = S[i:i+lt]
        for k, t in zip(tS, T):
            if k != t:
                tmp += 1
        ans = min(ans, tmp)
    print(ans)




if __name__ == "__main__":
    main()