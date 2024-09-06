def check_lucky_number(n):
  """Checks if a given number is a lucky number.

  A lucky number is a number that contains only the digits 4 and 7.

  Args:
    n: The number to check.

  Returns:
    True if the number is lucky, False otherwise.
  """

  count = 0
  while n != 0:
    if n % 10 == 4 or n % 10 == 7:
      count += 1
    n //= 10

  return count == 4 or count == 7

# Get input
n = int(input())

# Check if the number is lucky and print the result
if check_lucky_number(n):
  print("YES")
else:
  print("NO")
