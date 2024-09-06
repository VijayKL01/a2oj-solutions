def is_prime(num):
  """Checks if a given number is prime.

  Args:
    num: The number to check.

  Returns:
    True if the number is prime, False otherwise.
  """

  if num <= 1:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

if __name__ == "__main__":
  a, b = map(int, input().split())

  for i in range(a + 1, 0, -1):
    if is_prime(i):
      if i == b:
        print("YES")
      else:
        print("NO")
      break
