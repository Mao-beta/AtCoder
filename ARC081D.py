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
    S1 = SI()
    S2 = SI()
    ans = 1
    prev_a = S1[0]
    prev_b = S2[0]
    for i, (a, b) in enumerate(zip(S1, S2)):
        if i == 0:
            if a == b:
                ans *= 3
            else:
                ans *= 6
            continue
        if prev_a == a:
            continue

        if a == b and prev_a == prev_b:
            ans *= 2
        elif a == b and prev_a != prev_b:
            ans *= 1
        elif a != b and prev_a == prev_b:
            ans *= 2
        else:
            ans *= 3

        ans %= MOD
        prev_a = a
        prev_b = b

    print(ans)


if __name__ == "__main__":
    main()
