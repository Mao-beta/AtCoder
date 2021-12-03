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
    N = NI()
    A, B, C = NMI()
    ans = 10**4
    for i in range(N//A + 1):
        for j in range(N//B + 1):
            if i + j >= 10**4: break
            n = N - A*i - B*j
            if n < 0 or n % C >= 1: continue
            k = n // C
            ans = min(ans, i+j+k)
    print(ans)



if __name__ == "__main__":
    main()
