def count_invalid_numbers(n, arr):
 
  Args:
    n: The size of the array.
    arr: The array of integers.

  Returns:
    The count of invalid numbers.
  """

  sum_of_arr = sum(arr)

  count = 0
  for i in range(1, 6):
    if (i + sum_of_arr) % (n + 1) != 1:
      count += 1

  return count

if __name__ == "__main__":
  n = int(input())
  arr = list(map(int, input().split()))

  result = count_invalid_numbers(n, arr)
  print(result)
