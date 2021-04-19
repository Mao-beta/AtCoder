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
    A = sorted(list(set(NLI())))

    G = [A[0]]
    for i in range(len(A)-1):
        G.append(A[i+1] - A[i])

    ans = 1
    for g in G:
        ans = ans * (g+1) % MOD
    print(ans)



if __name__ == "__main__":
    main()
