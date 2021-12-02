import sys
from pathlib import Path
import random

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def output_ans(ans, path=None):
    if path:
        with open(path, "w") as f:
            for row in ans:
                f.write("".join(map(str, row)) + "\n")
    else:
        for row in ans:
            print(*row)


def main():
    N = 500
    M = 29
    L = 300
    dst_dir = Path("./in/")
    dst_dir.mkdir(exist_ok=True)
    S = "SSLR"


    for case in range(100):
        random.seed(case)
        filename = str(case).zfill(3) + ".in"

        lines = [f"{N} {M} {L}"]
        for i in range(N):
            line = ""
            for l in range(L):
                s = S[random.randint(0, 3)]
                line += s
            lines.append(line)

        output_ans(lines, dst_dir/filename)


if __name__ == "__main__":
    main()
