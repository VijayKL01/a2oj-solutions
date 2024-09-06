def compare_strings(a, b):
  """Compares two strings and prints the result as a binary string.

  Args:
    a: The first string.
    b: The second string.
  """

  for i in range(len(a)):
    if a[i] == b[i]:
      print(0, end="")
    else:
      print(1, end="")

# Get input
a, b = input().split()

# Compare strings and print the result
compare_strings(a, b)
