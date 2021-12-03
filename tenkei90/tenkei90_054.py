import sys
from collections import deque
from collections import defaultdict

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, M = NMI()
    P = defaultdict(list)
    for i in range(M):
        K = NI()
        R = NLI()
        center = 10**6 + i
        for x in R:
            P[x].append(center)
        P[center] = R.copy()

    T = defaultdict(lambda: -1)
    T[1] = 0

    queue = deque()
    queue.append(1)
    while queue:
        now = queue.popleft()
        S = P[now]
        t = T[now]

        for goto in S:
            if T[goto] != -1:
                continue
            T[goto] = t+1
            queue.append(goto)

    for x in range(1, N+1):
        print(T[x]//2 if T[x] != -1 else -1)


if __name__ == "__main__":
    main()
