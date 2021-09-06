import sys
from itertools import accumulate

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    RH = [NLI() for _ in range(N)]
    RC = [0] * 100001
    R0 = [0] * 100001
    R1 = [0] * 100001
    R2 = [0] * 100001
    for r, h in RH:
        RC[r] += 1
        if h == 1:
            R0[r] += 1
        elif h == 2:
            R1[r] += 1
        else:
            R2[r] += 1

    # Rcum[i]: i以下のRateの人数
    Rcum = list(accumulate(RC))

    for r, h in RH:
        win = Rcum[r-1]
        lose = N - Rcum[r]
        even = -1
        h -= 1
        if h == 0:
            win += R1[r]
            lose += R2[r]
            even += R0[r]
        elif h == 1:
            win += R2[r]
            lose += R0[r]
            even += R1[r]
        else:
            win += R0[r]
            lose += R1[r]
            even += R2[r]

        print(win, lose, even)


if __name__ == "__main__":
    main()
