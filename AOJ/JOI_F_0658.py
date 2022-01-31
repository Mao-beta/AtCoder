import sys

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())


def main():
    H, W = NMI()
    S = [SI() for _ in range(H)]
    O = [[0] * W for _ in range(H)]
    I = [[0] * W for _ in range(H)]
    ans = 0
    for h in range(H-1, -1, -1):
        for w in range(W-1, -1, -1):
            s = S[h][w]
            orb = O[h][w]
            ing = I[h][w]
            orb_n = orb + 1 * (s == "O")
            ing_n = ing + 1 * (s == "I")

            if s == "J":
                ans += orb * ing
            if w >= 1:
                O[h][w-1] = orb_n
            if h >= 1:
                I[h-1][w] = ing_n

    print(ans)


if __name__ == "__main__":
    main()
