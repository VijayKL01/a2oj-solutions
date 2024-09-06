def count_operations(t):
  """Counts the number of increment and decrement operations.

  Args:
    t: The number of operations.

  Returns:
    The final value of p.
  """

  p = 0
  for _ in range(t):
    x = input()
    if "++" in x:
      p += 1
    elif "--" in x:
      p -= 1

  return p

if __name__ == "__main__":
  t = int(input())

  result = count_operations(t)
  print(result)
