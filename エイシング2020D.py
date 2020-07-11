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


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    N = NI()
    X = SI()
    X_pop = X.count("1")
    X_plus = X_pop + 1
    X_minus = X_pop - 1

    RP = [pow(2, i, X_plus) for i in range(N+1)]
    if X_minus > 0:
        RM = [pow(2, i, X_minus) for i in range(N+1)]
    else:
        RM = [0] * (N+1)

    X = X[::-1]
    rem_p = 0
    rem_m = 0
    for i in range(N):
        if X[i] == "1":
            rem_p += RP[i]
            rem_m += RM[i]

    for i in range(N-1, -1, -1):
        if X[i] == "0":
            tmp = (rem_p + RP[i]) % X_plus
        elif X_minus >= 1:
            tmp = (rem_m - RM[i]) % X_minus
        else:
            print(0)
            continue
        ans = 1
        while tmp > 0:
            tmp = tmp % bin(tmp).count("1")
            ans += 1
        print(ans)






if __name__ == "__main__":
    main()