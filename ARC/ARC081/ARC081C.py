import sys
import math
from collections import Counter
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
    C = Counter(A)
    S = sorted(set(A), reverse=True)
    ans = 0
    for a in S:
        if C[a] >= 4:
            if ans == 0:
                print(a**2)
                exit()
            else:
                print(ans * a)
                exit()
        elif C[a] >= 2:
            if ans == 0:
                ans = a
            else:
                ans *= a
                print(ans)
                exit()

    print(ans)


if __name__ == "__main__":
    main()
