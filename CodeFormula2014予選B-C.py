import sys
import math
from collections import deque
import itertools

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    A = SI()
    B = SI()
    if sorted(A) != sorted(B):
        print("NO")
        exit()

    if len(A) == 2:
        if A == B:
            print("NO")
            exit()
        else:
            print("YES")
            exit()
    diff = 0
    AD = []
    BD = []
    same_flg = False
    for a, b in zip(A, B):
        if a != b:
            diff += 1
            AD.append(a)
            BD.append(b)
        else:
            same_flg = True

    if diff > 6:
        print("NO")
        exit()
    if diff == 0:
        print("YES")
        exit()

    seq = range(diff)
    seq_c = list(itertools.combinations(seq, 2))
    for seqs in itertools.product(seq_c, repeat=3):
        tmp = AD[:]
        for x, y in seqs:
            tmp[x], tmp[y] = tmp[y], tmp[x]
            if same_flg and tmp == BD:
                print("YES")
                exit()

        if tmp == BD:
            print("YES")
            exit()

    print("NO")


if __name__ == "__main__":
    main()