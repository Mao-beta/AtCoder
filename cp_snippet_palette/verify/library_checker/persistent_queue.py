# verification-helper: PROBLEM https://judge.yosupo.jp/problem/persistent_queue
import sys
from cp_snippet_palette.library.structures.persistent_queue import PersistentQueue


def main():
    read = sys.stdin.buffer.readline
    queue = PersistentQueue()
    answer = []
    for _ in range(int(read())):
        query = list(map(int, read().split()))
        if query[0] == 0:
            queue.append(query[1] + 1, query[2])
        else:
            version, value = queue.popleft(query[1] + 1)
            answer.append(str(value))
    print("\n".join(answer))


if __name__ == "__main__":
    main()
