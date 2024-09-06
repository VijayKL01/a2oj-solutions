def contains_h_q_or_9(s):
  """Checks if a string contains at least one of the characters 'H', 'Q', or '9'.

  Args:
    s: The input string.

  Returns:
    True if the string contains at least one of the specified characters, False otherwise.
  """

  for char in s:
    if char in "HQ9":
      return True

  return False

if __name__ == "__main__":
  s = input()

  if contains_h_q_or_9(s):
    print("YES")
  else:
    print("NO")
