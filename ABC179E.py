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
    N, X, M = NMI()
    A = []
    A_ID = {}
    break_flag = False
    start = 0
    end = N
    for i in range(M):
        if i == 0:
            A.append(X)
            A_ID[X] = 0
        else:
            x = A[-1]**2 % M
            if x not in A_ID:
                A.append(x)
                A_ID[x] = i
            else:
                A.append(x)
                start = A_ID[x]
                end = i
                break_flag = True
            if break_flag:
                break

    if N < start+1:
        print(sum(A[:N]))
        exit()

    ans = sum(A[:start])
    lp = sum(A[start:end])
    gap = end - start
    lp_n = (N - start) // gap
    rem = (N - start) % gap
    ans += lp * lp_n + sum(A[start: start + rem])
    print(ans)




if __name__ == "__main__":
    main()