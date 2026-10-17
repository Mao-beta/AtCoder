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

alp_to_num = {chr(i+97): i for i in range(26)}
ALP_to_num = {chr(i+97).upper(): i for i in range(26)}
num_to_alp = {i: chr(i+97) for i in range(26)}
num_to_ALP = {i: chr(i+97).upper() for i in range(26)}

def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    Q = NI()
    querys = [list(SI().split()) for _ in range(Q)]
    D = deque()
    for q in querys:
        if q[0] == "1":
            D.append([q[1], int(q[2])])
            continue

        cut = [0]*26
        d = int(q[1])
        while d > 0 and D:
            L = D.popleft()
            if d >= L[1]:
                cut[alp_to_num[L[0]]] += L[1]
                d -= L[1]
            else:
                cut[alp_to_num[L[0]]] += d
                D.appendleft([L[0], L[1] - d])
                d = 0
        ans = 0
        for c in cut:
            ans += c**2
        print(ans)




if __name__ == "__main__":
    main()