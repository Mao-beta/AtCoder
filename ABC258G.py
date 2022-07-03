import sys
import numpy as np

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD99 = 998244353

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())


def main():
    N = NI()
    A = [list(map(float, list(SI()))) for _ in range(N)]
    A = np.array(A)
    B = (A @ A) * A
    print(np.sum(B.astype(np.int64)) // 6)


def main_TLE():
    N = NI()
    A = [list(map(int, list(SI()))) for _ in range(N)]
    A = np.array(A)
    B = (A @ A) * A
    print(np.sum(B) // 6)


def main_TLE_():
    N = NI()
    A = [list(map(float, list(SI()))) for _ in range(N)]
    A = np.array(A)
    B = A @ A @ A
    print(np.trace(B.astype(np.int64)) // 6)


if __name__ == "__main__":
    main()
