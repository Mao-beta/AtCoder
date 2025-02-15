import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD99 = 998244353

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())
EI = lambda m: [NLI() for _ in range(m)]


def main():
    N = NI()
    A = NLI()
    C = Counter(A)
    MC = C.most_common()
    if MC[0][1] >= 2:
        x = MC[0][0]
        ans = []
        cnt = 0
        for a in A:
            if a == x:
                if cnt == 0:
                    ans.append(a)
                elif cnt == 1:
                    ans.append(-a)
                else:
                    ans.append(0)
                cnt += 1
            else:
                ans.append(0)
        print("Yes")
        print(*ans)

    else:
        B = min(N, 22)
        S = set()
        T = [0] * (1<<B)
        c = -1
        d = 0
        for case in range(1<<B):
            tmp = 0
            for i in range(B):
                if (case >> i) & 1:
                    tmp += A[i]
            if tmp in S:
                c = T.index(tmp)
                d = case
                break
            else:
                S.add(tmp)
                T[case] = tmp

        if c == -1:
            print("No")
            return

        ans = []
        for i, a in enumerate(A):
            if (c>>i) & 1:
                ans.append(a)
            elif (d>>i) & 1:
                ans.append(-a)
            else:
                ans.append(0)

        print("Yes")
        print(*ans)


if __name__ == "__main__":
    main()
