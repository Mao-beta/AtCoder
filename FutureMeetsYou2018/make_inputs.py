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


def main():
    K = list(range(1000, 3050, 50))
    A = list(range(1, 30001))
    dst_dir = Path("./in/")
    dst_dir.mkdir(exist_ok=True)

    for k in K:
        filename = f"in_K{k}.txt"
        random.shuffle(A)
        lines = []
        lines.append(f"30000 {k}\n")
        for a in A:
            lines.append(str(a)+"\n")

        with open(dst_dir/filename, mode="w", encoding="utf-8") as f:
            f.writelines(lines)


if __name__ == "__main__":
    main()
