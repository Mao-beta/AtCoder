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
    S = SI()
    ans = 0
    for i in range(10**4):
        num = str(i).zfill(4)
        is_ok = True
        for k in range(10):
            sk = S[k]
            if str(k) in num and sk == "x":
                is_ok = False
            if sk == "o" and str(k) not in num:
                is_ok = False
        if is_ok:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
