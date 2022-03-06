import sys
import math
from collections import deque

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    x = (N-6) // 6
    r = N % 6 + 6
    SIX = ["##..#.",
           "##..#.",
           "..##.#",
           "..##.#",
           "##...#",
           "..###."]

    SEVEN = ["##....#",
             "##....#",
             "..##.#.",
             "..###..",
             "...###.",
             "..#.##.",
             "##....#"]

    EIGHT = [".##....#",
             "##....#.",
             "#.##....",
             "..#.##..",
             "...##..#",
             "...#..##",
             ".#...##.",
             "#...##.."]

    NINE = [".##.....#",
            "#.#....#.",
            "###......",
            "...###...",
            "...#.#..#",
            "...###...",
            "......###",
            ".#..#.#..",
            "#.....##."]

    TEN = [".##.....#.",
           "###.......",
           "###.......",
           "...##....#",
           "...##....#",
           ".....##.#.",
           ".....###..",
           "......###.",
           "#....#.#..",
           "...##....#"]

    ELEVEN = ["###........",
              "###........",
              "###........",
              "....##....#",
              "...##....#.",
              "...#..#..#.",
              ".....#.##..",
              "......##..#",
              "......#..##",
              "....##..#..",
              "...#...##.."]


    ans = [["."]*N for _ in range(N)]
    H, W = 0, 0
    for xx in range(x):
        for h in range(H, H+6):
            for w in range(W, W+6):
                if SIX[h%6][w%6] == "#":
                    ans[h][w] = "#"
        H += 6
        W += 6

    D = {6: SIX, 7: SEVEN, 8: EIGHT, 9: NINE, 10: TEN, 11: ELEVEN}
    T = D[r]
    for h in range(H, H+r):
        for w in range(W, W+r):
            if T[h-H][w-W] == "#":
                ans[h][w] = "#"

    for row in ans:
        print("".join(row))


if __name__ == "__main__":
    main()
