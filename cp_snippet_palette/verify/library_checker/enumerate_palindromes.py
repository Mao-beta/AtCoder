# verification-helper: PROBLEM https://judge.yosupo.jp/problem/enumerate_palindromes
import sys
from cp_snippet_palette.library.strings.matching import manacher


def main():
    read = sys.stdin.buffer.readline
    s = read().strip()
    odd, even = manacher(s)
    answer = []
    for i in range(len(s)):
        if i:
            answer.append(2 * even[i])
        answer.append(2 * odd[i] - 1)
    print(*answer)


if __name__ == "__main__":
    main()
