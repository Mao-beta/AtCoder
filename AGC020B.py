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
    K = NI()
    A = NLI()
    A = A[::-1]
    m, M = 2, 2
    for a in A:
        pm, pM = m, M
        if m % a != 0:
            m += a - (m % a)
        if M % a != 0:
            M -= M % a
        if not (pm <= m <= pM and pm <= M <= pM):
            print(-1)
            exit()

        M += a-1
    print(m, M)



if __name__ == "__main__":
    main()
