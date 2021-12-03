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
    C1 = [0]
    C2 = [0]
    for i in range(N):
        c, p = NMI()
        if c == 1:
            C1.append(p)
            C2.append(0)
        else:
            C1.append(0)
            C2.append(p)

    C1 = list(accumulate(C1))
    C2 = list(accumulate(C2))
    Q = NI()
    for _ in range(Q):
        l, r = NMI()
        a1 = C1[r] - C1[l-1]
        a2 = C2[r] - C2[l-1]
        print(a1, a2)


if __name__ == "__main__":
    main()
