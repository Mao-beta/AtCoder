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
    A = NLI()

    former = A[:2**N//2]
    latter = A[2**N//2:]
    fmax = max(former)
    lmax = max(latter)
    f_idx = former.index(fmax)
    l_idx = latter.index(lmax) + 2**N//2
    if fmax > lmax:
        print(l_idx+1)
    else:
        print(f_idx+1)



if __name__ == "__main__":
    main()
