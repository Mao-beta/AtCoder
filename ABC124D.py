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
    N, K = NMI()
    S = SI()
    cnt = 0
    hand = []
    stand = []
    prev = "2"
    for i, s in enumerate(S):
        if s != prev and i != 0:
            if prev == "0":
                stand.append(cnt)
            else:
                hand.append(cnt)
            cnt = 0
        cnt += 1
        prev = s

    if cnt >= 1:
        if s == "0":
            stand.append(cnt)
        else:
            hand.append(cnt)

    if K >= len(stand):
        print(N)
        exit()

    SK = []
    SK.append(sum(stand[0:K]))
    for i in range(1, len(stand)):
        if i + K > len(stand):
            break
        SK.append(SK[-1] + stand[i-1+K] - stand[i-1])
    print(SK)




if __name__ == "__main__":
    main()