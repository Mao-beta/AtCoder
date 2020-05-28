X = int(input())

for a in range(100):
    for b in range(-100, 0):
        if X == a**5 - b**5:
            print(str(a) + " " + str(b))
            exit()

for t in range(200):
    for b in range(200):
        ans = t * (b**4*5 + b**3*t*10 + b**2*t**2*10 + b*t**3*5 + t**4)
        if X == ans:
            a = b + t
            print(str(a) + " " + str(b))
            exit()