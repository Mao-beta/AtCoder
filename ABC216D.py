import sys
import math
from collections import defaultdict
from collections import deque
from collections import Counter

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, M = NMI()
    D = defaultdict(list)
    T = []
    tops = Counter()
    for i in range(M):
        k = NI()
        A = NLI()
        for a in A:
            D[a].append(i)
        T.append(A)
        tops[A[0]] += 1

    idxs = [0] * M
    while tops:
        c, m = tops.most_common(1)[0]
        if m == 0:
            print("Yes")
            exit()
        if m < 2:
            print("No")
            exit()

        p, q = D[c]
        idxs[p] += 1
        idxs[q] += 1
        tops[c] -= 2
        try:
            tops[T[p][idxs[p]]] += 1
        except:
            pass
        try:
            tops[T[q][idxs[q]]] += 1
        except:
            pass

    print("Yes")



if __name__ == "__main__":
    main()
