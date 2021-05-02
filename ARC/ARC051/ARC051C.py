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
    N, A, B = NMI()
    AI = sorted(NLI())

    if A == 1:
        print(*AI, sep="\n")
        exit()

    max_a = AI[-1]
    cnt = 0
    while min(AI) * A <= max_a:
        AI[0] *= A
        cnt += 1
        AI.sort()

        if cnt == B:
            print(*[a % MOD for a in AI], sep="\n")
            exit()

    B -= cnt
    loop = B // N
    rem = B % N
    for _ in range(rem):
        AI[0] *= A
        AI.sort()
    for a in AI:
        print(a * pow(A, loop, MOD) % MOD)



if __name__ == "__main__":
    main()
