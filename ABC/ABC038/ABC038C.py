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


def main():
    N = NI()
    A = NLI()
    print(syakutori(A))

# 狭義単調増加列のカウント
def syakutori(array):
    n = len(array)
    r = 1
    res = 0
    for l in range(n):
        while 0 < r < n and (r <= l or array[r] > array[r-1]):
            r += 1
        res += r-l
        if l == r:
            r += 1

    return res


if __name__ == "__main__":
    main()