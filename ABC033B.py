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


def main():
    N = NI()
    total = 0
    max_name = ""
    max_num = 0
    for _ in range(N):
        s, p = SI().split()
        p = int(p)
        total += p
        if p > max_num:
            max_name = s
            max_num = p

    if max_num > total // 2:
        print(max_name)
    else:
        print("atcoder")


if __name__ == "__main__":
    main()
