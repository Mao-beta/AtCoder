import sys
import math
from itertools import combinations

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, P, Q = NMI()
    A = NLI()

    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                for l in range(k+1, N):
                    for m in range(l+1, N):
                        if A[i]*A[j]%P*A[k]%P*A[l]%P*A[m]%P == Q:
                            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
