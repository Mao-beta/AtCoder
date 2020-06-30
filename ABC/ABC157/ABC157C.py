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
    N, M = NMI()
    query = [NLI() for _ in range(M)]
    numbers = list(range(10**(N-1), 10**N))
    if N == 1: numbers = [0] + numbers
    for n in numbers:
        s = str(n)
        ok = True
        for q in query:
            if s[q[0]-1] == str(q[1]):
                continue
            else:
                ok = False
        if ok:
            print(n)
            exit()
    print(-1)

if __name__ == "__main__":
    main()