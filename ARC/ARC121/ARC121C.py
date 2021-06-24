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


def main():
    T = NI()
    for _ in range(T):
        N = NI()
        P = NLI()
        P = [p-1 for p in P]
        #print(P)

        now = 1
        ans = []
        for k in range(N):
            ki = P.index(k)

            while P[k] != k:
                #print(now, k, ki)
                #print(P)
                if now % 2 == 1:
                    if ki % 2 == 1:
                        is_ok = True
                    else:
                        is_ok = False
                else:
                    if ki % 2 == 0:
                        is_ok = True
                    else:
                        is_ok = False

                if is_ok:
                    x = ki-1
                    ki -= 1
                else:
                    if now % 2 == 1 and N % 2 == 1:
                        x = N-3
                    elif now % 2 == 1 and N % 2 == 0:
                        x = N-2
                    elif now % 2 == 0 and N % 2 == 1:
                        x = N-2
                    elif now % 2 == 0 and N % 2 == 0:
                        x = N-3
                    if x == ki:
                        ki += 1
                    elif x+1 == ki:
                        ki -= 1
                ans.append(x+1)
                P[x], P[x+1] = P[x+1], P[x]
                now += 1

            if sorted(P) != P:
                for k in range(N):
                    ki = P.index(k)

                    while P[k] != k:
                        # print(now, k, ki)
                        # print(P)
                        if now % 2 == 1:
                            if ki % 2 == 1:
                                is_ok = True
                            else:
                                is_ok = False
                        else:
                            if ki % 2 == 0:
                                is_ok = True
                            else:
                                is_ok = False

                        if is_ok:
                            x = ki - 1
                            ki -= 1
                        else:
                            if now % 2 == 1 and N % 2 == 1:
                                x = N - 3
                            elif now % 2 == 1 and N % 2 == 0:
                                x = N - 2
                            elif now % 2 == 0 and N % 2 == 1:
                                x = N - 2
                            elif now % 2 == 0 and N % 2 == 0:
                                x = N - 3
                            if x == ki:
                                ki += 1
                            elif x + 1 == ki:
                                ki -= 1
                        ans.append(x + 1)
                        P[x], P[x + 1] = P[x + 1], P[x]
                        now += 1
        print(len(ans))
        print(*ans)



if __name__ == "__main__":
    main()
