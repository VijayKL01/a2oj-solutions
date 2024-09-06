def find_min_difference(arr):
  """Finds the minimum difference between adjacent elements in an array.

  Args:
    arr: The array of integers.

  Returns:
    A tuple containing the indices of the elements with the minimum difference.
  """

  n = len(arr)
  min_diff = abs(arr[0] - arr[1])
  min_indices = (1, 2)

  for i in range(1, n - 1):
    diff = abs(arr[i] - arr[i + 1])
    if diff < min_diff:
      min_diff = diff
      min_indices = (i + 1, i + 2)

  if abs(arr[0] - arr[n - 1]) < min_diff:
    min_indices = (n, 1)

  return min_indices

if __name__ == "__main__":
  n = int(input())
  arr = list(map(int, input().split()))

  result = find_min_difference(arr)
  print(*result)
