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


def count_inversion(sequence):
    return sum(sum(m<n for m in sequence[i+1:]) for i,n in enumerate(sequence))


def main():
    N = NI()
    P = [0] + NLI()

    IDX = [0] * (N+1)
    for i, p in enumerate(P):
        IDX[p] = i
    #print(IDX)

    ans = []
    cnt = 0
    flag = False
    for i in range(1, N):
        idx = IDX[i]
        if i == idx:
            continue
        for j in range(idx, i, -1):
            #print(j-1)
            ans.append(j-1)
            cnt += 1
            IDX[P[j-1]], IDX[P[j]] = IDX[P[j]], IDX[P[j-1]]
            P[j-1], P[j] = P[j], P[j-1]
            #print(IDX)
            #print(P)
            if cnt == N-1:
                flag = True
                break
        if flag:
            break

    if P == [i for i in range(N+1)] and len(set(ans)) == N-1:
        print(*ans, sep="\n")
    else:
        print(-1)



if __name__ == "__main__":
    main()
