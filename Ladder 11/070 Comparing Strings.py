def is_valid_string(s1, s2):
  """Checks if two strings are valid strings.

  A valid string is a string where at most two characters differ, and if there are two differences, they must be the same character in each string.

  Args:
    s1: The first string.
    s2: The second string.

  Returns:
    True if the strings are valid, False otherwise.
  """

  if len(s1) != len(s2):
    return False

  count = 0
  c1, c2 = None, None

  for i in range(len(s1)):
    if s1[i] != s2[i]:
      count += 1
      if count == 1:
        c1, c2 = s1[i], s2[i]
      elif count == 2:
        if s1[i] != c1 or s2[i] != c2:
          return False

  return count == 2 and s1[i] == c2 and s2[i] == c1

if __name__ == "__main__":
  t = int(input())

  for _ in range(t):
    s1, s2 = input().split()

    if is_valid_string(s1, s2):
      print("YES")
    else:
      print("NO")
