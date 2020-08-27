import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def syakutori(array):
    n = len(array)
    r = 1
    res = 0
    now = array[0]
    for l in range(n):
        while 0 < r < n and now^array[r] == now+array[r]:
            now = now ^ array[r]
            r += 1
        res += r-l
        now = now ^ array[l]

        if l == r:
            r += 1

    return res


def main():
    N = NI()
    A = NLI()
    print(syakutori(A))


if __name__ == "__main__":
    main()