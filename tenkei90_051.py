import sys
import math
from itertools import accumulate
from collections import defaultdict
import bisect

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, K, P = NMI()
    A = NLI()
    X = A[:N//2]
    Y = A[N//2:]

    def make_all_case(X):
        res = defaultdict(list)
        n = len(X)
        for case in range(1<<n):
            tmp = 0
            k = bin(case).count("1")
            for i, x in enumerate(X):
                if (case >> i) & 1:
                    tmp += x
            res[k].append(tmp)

        for k in range(n+1):
            res[k].sort()

        return res

    BX = make_all_case(X)
    BY = make_all_case(Y)

    ans = 0
    for k in range(K+1):
        BXK = BX[k]
        BYK = BY[K-k]
        for x in BXK:
            idx = bisect.bisect_right(BYK, P-x)
            ans += idx

    print(ans)


if __name__ == "__main__":
    main()
