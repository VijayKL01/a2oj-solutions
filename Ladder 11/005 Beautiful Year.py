def find_next_pandigital_number(x):
  """Finds the next pandigital number greater than x.

  A pandigital number is a number that contains all digits from 0 to 9 at least once.

  Args:
    x: The starting number.

  Returns:
    The next pandigital number greater than x.
  """

  while True:
    x += 1
    digits = [int(digit) for digit in str(x)]
    if len(set(digits)) == len(digits):
      return x

# Get input
x = int(input())

# Find the next pandigital number and print the result
result = find_next_pandigital_number(x)
print(result)
