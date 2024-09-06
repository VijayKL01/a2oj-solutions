def count_max_min_updates(n, a):
  """Counts the number of times the maximum and minimum values are updated in an array.

  Args:
    n: The size of the array.
    a: The array of integers.

  Returns:
    The count of updates.
  """

  max_val = a[0]
  min_val = a[0]
  count = 0

  for i in range(1, n):
    if a[i] > max_val:
      max_val = a[i]
      count += 1
    elif a[i] < min_val:
      min_val = a[i]
      count += 1

  return count

if __name__ == "__main__":
  n = int(input())
  a = list(map(int, input().split()))

  result = count_max_min_updates(n, a)
  print(result)
