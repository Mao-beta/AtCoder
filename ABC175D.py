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


def make_cumulative(A):
    C = [0] * (len(A) + 1)
    for i, a in enumerate(A):
        i += 1
        C[i] = C[i - 1] + a
    return C


def main():
    N, K = NMI()
    P = NLI()
    P = [p-1 for p in P]
    C = NLI()

    seen = [0] * N
    loops = []
    for i in range(N):
        if seen[i] == 1:
            continue
        now = i
        now_loop = [now]
        now_cost = C[now]
        while True:
            seen[now] = 1
            goto = P[now]
            if seen[goto] == 1:
                break
            now_loop.append(goto)
            now_cost += C[goto]
            now = goto
        loops.append([now_loop, now_cost])

    ans = -float("inf")
    for loop, cost in loops:
        C_cum = make_cumulative([C[p] for p in loop])

        for i, start in enumerate(loop):
            for j, end in enumerate(loop):
                if i == j:
                    base = cost
                    moved = len(loop)
                elif i < j:
                    base = C_cum[j] - C_cum[i]
                    moved = j - i
                else:
                    base = cost - (C_cum[i] - C_cum[j])
                    moved = len(loop) + j - i

                if moved > K:
                    continue

                if cost > 0:
                    tmp_K = K - moved
                    num_loop = tmp_K // len(loop)
                    tmp_ans = num_loop * cost + base
                else:
                    tmp_ans = base

                ans = max(ans, tmp_ans)

    print(ans)



if __name__ == "__main__":
    main()