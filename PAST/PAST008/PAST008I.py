import sys
from heapq import heappush, heappop, heapify

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    A = NLI()

    K = 0
    for i in range(N):
        while A[i] % 2 == 0:
            A[i] //= 2
            K += 1

    hq = A[:]
    heapify(hq)
    for i in range(K):
        m = heappop(hq)
        heappush(hq, m*3)

    print(heappop(hq))


if __name__ == "__main__":
    main()
