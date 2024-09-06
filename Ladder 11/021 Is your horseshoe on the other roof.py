def count_duplicates(arr):
  """Counts the number of duplicate elements in an array.

  Args:
    arr: The array of integers.

  Returns:
    The count of duplicates.
  """

  count = 0
  for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
      if arr[i] == arr[j]:
        count += 1
        break

  return count

if __name__ == "__main__":
  arr = list(map(int, input().split()))

  result = count_duplicates(arr)
  print(result)
