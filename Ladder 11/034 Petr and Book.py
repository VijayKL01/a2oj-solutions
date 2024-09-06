def find_minimum_days(num, arr):

  sum = 0
  for i in range(7):
    sum += arr[i]

  if sum < num:
    return -1

  for i in range(7):
    if sum >= num:
      return i + 1
    sum -= arr[i]
    sum += arr[(i + 1) % 7]

  return -1

if __name__ == "__main__":
  num = int(input())
  arr = list(map(int, input().split()))

  result = find_minimum_days(num, arr)
  print(result)
