import sys


NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())
EI = lambda m: [NLI() for _ in range(m)]


def main():
    N, M, K = NLI()
    T = list(SI())
    S = [list(int(s == T[i]) for i, s in enumerate(SI())) for _ in range(N)]
    Q = NI()
    IJ = EI(Q)
    IJ = [[x-1, y-1] for x, y in IJ]

    trie = [[-1, -1, 0]]
    for s in S:
        now = 0
        for ss in s:
            l, r, val = trie[now]
            trie[now][-1] += 1
            if ss == 0:
                if l == -1:
                    trie.append([-1, -1, 0])
                    trie[now][0] = len(trie) - 1
                    now = trie[now][0]
                else:
                    now = trie[now][0]
            else:
                if r == -1:
                    trie.append([-1, -1, 0])
                    trie[now][1] = len(trie) - 1
                    now = trie[now][1]
                else:
                    now = trie[now][1]
        trie[now][-1] += 1

    # print(trie)

    for i, j in IJ:
        # 消す
        now = 0
        for ss in S[i]:
            trie[now][-1] -= 1
            if ss == 0:
                now = trie[now][0]
            else:
                now = trie[now][1]
        trie[now][-1] -= 1

        S[i][j] ^= 1

        # 足す
        now = 0
        for ss in S[i]:
            l, r, val = trie[now]
            trie[now][-1] += 1
            if ss == 0:
                if l == -1:
                    trie.append([-1, -1, 0])
                    trie[now][0] = len(trie) - 1
                    now = trie[now][0]
                else:
                    now = trie[now][0]
            else:
                if r == -1:
                    trie.append([-1, -1, 0])
                    trie[now][1] = len(trie) - 1
                    now = trie[now][1]
                else:
                    now = trie[now][1]
        trie[now][-1] += 1

        # check
        now = 0
        passed = 0
        ok = False
        # print(trie)
        for ss in S[i]:
            l, r, val = trie[now]
            # print(now, l, r, par, val, passed)
            if r == -1:
                now = l
            elif passed + trie[r][-1] <= M:
                passed += trie[r][-1]
                if ss == 1:
                    ok = True
                    break
                else:
                    now = l
            else:
                if ss == 0:
                    ok = False
                    break
                else:
                    now = r

        # print(i, j, trie)
        if ok:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
