def main():
    a, b, c = map(int, input().split())
    m = a * b * c
    mod = 1073741824

    arr = [0] * (m + 1)
    for i in range(1, m + 1):
        for j in range(i, m + 1, i):
            arr[j] += 1

    ans = 0
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            for k in range(1, c + 1):
                ans += arr[i * j * k]
                ans %= mod

    print(ans)

if __name__ == "__main__":
    main()
