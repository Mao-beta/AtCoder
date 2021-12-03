import sys
import math
from itertools import product

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    C = list(product([1, -1], repeat=N))

    for c in C:
        if sum(c) != 0:
            continue

        s = 0
        ans = ""
        is_ok = True
        for x in c:
            s += x
            ans += "(" if x == 1 else ")"
            if s < 0:
                is_ok = False
        if is_ok:
            print(ans)


if __name__ == "__main__":
    main()
