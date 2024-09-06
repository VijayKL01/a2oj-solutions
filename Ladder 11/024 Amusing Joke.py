def check_anagrams(a, b, c):
  """Checks if the concatenation of two strings is an anagram of the third string.

  Args:
    a: The first string.
    b: The second string.
    c: The third string.

  Returns:
    "YES" if the concatenation is an anagram, "NO" otherwise.
  """

  ab = a + b
  if len(ab) != len(c):
    return "NO"

  sorted_ab = sorted(ab)
  sorted_c = sorted(c)

  return "YES" if sorted_ab == sorted_c else "NO"

if __name__ == "__main__":
  a, b, c = input().split()

  result = check_anagrams(a, b, c)
  print(result)
