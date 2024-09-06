def find_minimum_index(n, k, arr):


  arr[k - 1:] = sorted(arr[k - 1:])

  if arr[k - 1] != arr[n - 1]:
    return -1

  for i in range(k - 1, 0, -1):
    if arr[i] != arr[i - 1]:
      return i

  return -1

if __name__ == "__main__":
  t = int(input())

  for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    result = find_minimum_index(n, k, arr)
    print(result)
