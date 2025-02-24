from collections import deque
H, W, M = map(int, input().split())
RCS = [list(map(int, input().split())) for _ in range(M)]
INF = 1000
G = [INF]*(H*W)

def f(g, r, c):
    return (g+INF)*INF**2 + r*INF + c
def inv(grc):
    gr, c = divmod(grc, INF)
    g, r = divmod(gr, INF)
    g -= INF
    return g, r, c

DH = [1, -1, 0, 0]
DW = [0, 0, 1, -1]
D = deque()
for r, c, s in RCS:
    r -= 1
    c -= 1
    G[r*W+c] = -(s+1)
    D2 = deque()
    D2.append(r*W+c)
    while D2:
        h, w = divmod(D2.popleft(), W)
        print(h, w)
        g = G[h*W+w]
        for dh, dw in zip(DH, DW):
            nh, nw = h+dh, w+dw
            if not(0 <= nh < H and 0 <= nw < W):
                continue
            if G[nh*W+nw] <= g:
                continue
            if g+1 == 0:
                D.append(nh*W+nw)
                G[nh*W+nw] = g+1
            else:
                D2.append(nh*W+nw)
                G[nh*W+nw] = g+1
print("#")
while D:
    h, w = divmod(D.popleft(), W)
    print(h, w)
    g = G[h*W+w]
    for dh, dw in zip(DH, DW):
        nh, nw = h+dh, w+dw
        if not(0 <= nh < H and 0 <= nw < W):
            continue
        if G[nh*W+nw] <= g+1:
            continue
        D.append(nh*W+nw)
        G[nh*W+nw] = g+1
ans = max(G)
print(ans)