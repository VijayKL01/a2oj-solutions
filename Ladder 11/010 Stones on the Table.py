def count_consecutive_characters(s):
 

  Args:
    s: The input string.

  Returns:
    The count of consecutive characters.
  """

  count = 0
  for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
      count += 1

  return count


n = int(input())
c = input()

# Count consecutive characters and print the result
result = count_consecutive_characters(c)
print(result)
