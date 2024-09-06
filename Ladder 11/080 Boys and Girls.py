def main():
    a, b = map(int, input().split())
    c = max(a, b)
    d = min(a, b)

    if c == d:
        p, q = "G", "B"
    elif a < b:
        p, q = "G", "B"
    else:
        p, q = "B", "G"

    for i in range(1, c + 1):
        if i <= c:
            print(p, end='')
        if i <= d:
            print(q, end='')

if __name__ == "__main__":
    main()
