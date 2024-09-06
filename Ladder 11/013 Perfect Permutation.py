def print_even_numbers(n):
  """Prints even numbers from 1 to n in pairs.

  Args:
    n: The upper limit.
  """

  if n % 2 == 0:
    for i in range(1, n, 2):
      print(i + 1, i, end=" ")

if __name__ == "__main__":
  n = int(input())

  if n % 2 == 1:
    print("-1")
  else:
    print_even_numbers(n)
