import sys
import bisect
from itertools import accumulate

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, X = NMI()
    L = [0] + NLI()
    D = list(accumulate(L))
    idx = bisect.bisect_right(D, X)
    print(idx)


if __name__ == "__main__":
    main()
