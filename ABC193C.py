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
    can_set = set()
    for a in range(2, 10**5 + 2):
        for b in range(2, 10**5 + 2):
            if a**b > N:
                break
            can_set.add(a**b)
    print(N - len(can_set))



if __name__ == "__main__":
    main()
