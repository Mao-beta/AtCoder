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


num_to_alp = {i: chr(i+97) for i in range(26)}


def main():
    P = NLI()
    ans = [num_to_alp[p-1] for p in P]
    print("".join(ans))


if __name__ == "__main__":
    main()
