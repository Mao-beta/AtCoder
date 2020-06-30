import bisect
N = int(input())
H = []
S = []
for i in range(N):
    h, s = map(int, input().split())
    H.append(h)
    S.append(s)

ng = -1
ok = 1000000000 + 100000*10000000000
mid = (ng + ok) // 2
# 各H, Sについてmid以下にするには何秒後までに撃つかを算出
# H + S * t <= mid
# t <= (mid - H) // S
# tを連想配列にして上から累積和にして1,2,3...と比較？ O(n)

while abs(ng - ok) > 1:
    times = []
    mid = (ng + ok) // 2
    for i in range(N):
        times.append((mid - H[i]) // S[i])
    times = sorted(times)
    ngflag = False
    for i, t in enumerate(times):
        if i > t:
            ngflag = True
            break

    if ngflag:
        ng = mid
    else:
        ok = mid

print(ok)