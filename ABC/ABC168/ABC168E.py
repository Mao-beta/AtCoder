import math
import bisect
MOD = 1000000007
N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
deg = []
for a, b in AB:
    if a == 0 and b == 0:
        deg.append(3600.0)
        continue
    deg.append(math.degrees(math.atan2(b,a)))

deg = sorted(deg)
print(deg)
matches = []
origin = 0
flags = [0] * N
for i, d in enumerate(deg):
    if flags[i]:
        continue
    if d == 3600.0:
        origin += 1
        continue

    minus_deg = d - 90
    plus_deg = d + 90
    match = 0
    if minus_deg >= -180.0:
        L_idx = bisect.bisect_left(deg, minus_deg)
        R_idx = bisect.bisect_right(deg, minus_deg)
        match += R_idx - L_idx
        flags[L_idx:R_idx] = [1] * (R_idx - L_idx)
    if plus_deg <= 180.0:
        L_idx = bisect.bisect_left(deg, plus_deg)
        R_idx = bisect.bisect_right(deg, plus_deg)
        match += R_idx - L_idx
        flags[L_idx:R_idx] = [1] * (R_idx - L_idx)
    if match:
        matches.append(match+1)

print(matches)
normal = N - sum(matches) - origin

ans = 1
for i in range(len(matches)):
    ans *= matches[i] + 1
    ans %= MOD
ans *= 2 ** normal
ans %= MOD
ans -= 1
if origin:
    ans += 1
print(ans)
