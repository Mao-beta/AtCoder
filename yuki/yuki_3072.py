import os
import math

def main():
    dat = os.read(0, 20000010).decode().split('\n')
    ans = 0
    for x in dat[1:-1]:
        x = int(x)
        ans += int(math.sqrt(x) * 10**22)
        d = str(ans // 10**22)
        s = str(ans)[:len(d)] + "." + str(ans)[len(d):]
        print(s[:19])


if __name__ == "__main__":
    main()
