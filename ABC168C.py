import math
A, B, H, M = map(int, input().split())
time = 60 * H + M
angle = 5.5 * time - (5.5 * time // 360 * 360)
angle = min(angle, 360 - angle)
cos_a = math.cos(math.radians(angle))
c2 = A**2 + B**2 - 2*A*B*cos_a
print(math.sqrt(c2))