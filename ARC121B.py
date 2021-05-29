import sys
from heapq import heapify, heappop, heappush
from collections import Counter

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    dogs = []
    colors = []

    for i in range(2*N):
        a, c = SI().split()
        a = int(a)
        dogs.append([a, c, i])
        colors.append(c)

    C = Counter(colors)

    if C["R"] % 2 == 0 and C["G"] % 2 == 0 and C["B"] % 2 == 0:
        print(0)
        exit()

    if C["R"] % 2 == 0:
        even = "R"
        odd_a, odd_b = "G", "B"
    elif C["G"] % 2 == 0:
        even = "G"
        odd_a, odd_b = "R", "B"
    else:
        even = "B"
        odd_a, odd_b = "R", "G"

    dogs.sort()

    gaps = []
    heapify(gaps)
    for i in range(2*N-1):
        d1, d2 = dogs[i], dogs[i+1]
        if d1[1] != d2[1]:
            heappush(gaps, [abs(d1[0]-d2[0]), {d1[2], d2[2]}, {d1[1], d2[1]}])

    D = {"ea": [], "eb": [], "ab": []}
    while gaps:
        gap, idx, color = heappop(gaps)
        if color == {even, odd_a}:
            key = "ea"
        elif color == {even, odd_b}:
            key = "eb"
        else:
            key = "ab"

        if len(D[key]) < 3:
            D[key].append([gap, idx])

    if D["ab"]:
        ans = D["ab"][0][0]
    else:
        ans = 10**20

    kouho = []
    for gea, eaidx in D["ea"]:
        for geb, ebidx in D["eb"]:
            if (eaidx & ebidx):
                continue
            g = gea + geb
            kouho.append(g)

    kouho.sort()
    if kouho:
        ans = min(ans, kouho[0])

    print(ans)


if __name__ == "__main__":
    main()
