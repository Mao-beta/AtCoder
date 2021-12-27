import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD99 = 998244353
INF = 1001001

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())


def main():
    N, D = NMI()
    A = NLI()
    A = [x-1 if x > 0 else -1 for x in A]
    R = 2 * D + 1

    # print(A)

    # check
    for i, a in enumerate(A):
        if a == -1:
            continue
        if abs(a - i) > D:
            print(0)
            exit()


    dp = [[0]*(1<<R) for _ in range(N+1)]
    focus = deque()
    for _ in range(D):
        focus.append(INF)
    for i in range(D+1):
        try:
            focus.append(A[i])
        except:
            focus.append(INF)


    def deq_to_state(deq):
        deq = deq.copy()
        res = 0
        for i, x in enumerate(deq):
            if x != -1:
                res |= (1 << i)
        return res

    state = deq_to_state(focus)
    dp[0][state] = 1

    for i in range(N):
        # print(focus)
        state = deq_to_state(focus)
        # print(bin(state)[2:].zfill(R)[::-1])

        for j in range(1<<R):
            if dp[i][j] <= 0:
                continue

            if i in focus:
                # 次のfocusに合わせる
                nj = j >> 1
                # 新しいのが埋まってたら1、空いてたら0
                try:
                    a = A[i+1+D]
                    if a != -1:
                        nj |= 1 << (R-1)
                except:
                    nj |= 1 << (R - 1)

                dp[i+1][nj] += dp[i][j]
                dp[i+1][nj] %= MOD99

                # print([i, bin(j)[2:].zfill(R)[::-1]], [i+1, bin(nj)[2:].zfill(R)[::-1]])
                continue

            
            for k in range(R):
                if (j >> k) & 1:
                    continue

                # k番目を立てる
                nj = j | (1 << k)
                # 次のfocusに合わせる
                nj = nj >> 1
                # 新しいのが埋まってたら1、空いてたら0
                try:
                    a = A[i+1+D]
                    if a != -1:
                        nj |= 1 << (R-1)
                except:
                    nj |= 1 << (R - 1)
                
                dp[i+1][nj] += dp[i][j]
                dp[i+1][nj] %= MOD99

                # print([i, bin(j)[2:].zfill(R)[::-1]], [i+1, bin(nj)[2:].zfill(R)[::-1]])
                
                if k == 0:
                    break

        # focusをずらす
        focus.popleft()
        try:
            focus.append(A[i+1+D])
        except:
            focus.append(INF)

    # print(*dp, sep="\n")
    print(dp[N][-1])


if __name__ == "__main__":
    main()
