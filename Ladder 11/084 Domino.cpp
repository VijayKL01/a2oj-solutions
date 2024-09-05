def main():
    n = int(input())
    l, r = 0, 0
    s = False
    for _ in range(n):
        x, y = map(int, input().split())
        if n == 1 and (x % 2 + y % 2) == 1:
            print(-1)
            return
        if (x % 2 + y % 2) == 1:
            s = True
        l += x
        r += y
    if l % 2 == 0 and r % 2 == 0:
        print(0)
    elif l % 2 == 1 and r % 2 == 1 and s:
        print(1)
    else:
        print(-1)

if __name__ == "__main__":
    main()
