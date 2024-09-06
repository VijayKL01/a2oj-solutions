def find_max_min_coins(n, m, arr):
 

  arr.sort(reverse=True)
  arr2 = arr.copy()
  arr2.sort()

  max_coins = 0
  min_coins = 0

  for i in range(m):
    while n > 0 and arr[i] > 0:
      max_coins += 1
      arr[i] -= 1
      n -= 1

  n = m
  for i in range(m):
    while n > 0 and arr2[i] > 0:
      min_coins += 1
      arr2[i] -= 1
      n -= 1

  return max_coins, min_coins

if __name__ == "__main__":
  n, m = map(int, input().split())
  arr = list(map(int, input().split()))

  max_coins, min_coins = find_max_min_coins(n, m, arr)
  print(max_coins, min_coins)
