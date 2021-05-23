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
    A = NLI()
    Ms = [A[0]]
    for i in range(1, N):
        Ms.append(max(Ms[-1], A[i]))

    AS = list(accumulate([0]+A))

    ASS = list(accumulate(AS))

    for i, (a, b, c) in enumerate(zip(AS[1:], Ms, ASS)):
        print(a + b*(i+1) + c)



if __name__ == "__main__":
    main()
