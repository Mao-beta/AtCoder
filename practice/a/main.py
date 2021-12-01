#!/usr/bin/env pypy3


def main():
    a = int(input())
    b, c = (int(z) for z in input().split())
    s = input()
    print(a + b + c, s)


if __name__ == '__main__':
    main()