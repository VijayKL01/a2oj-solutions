def convert_case(word):
  """Converts a given word to uppercase if it has more uppercase letters, or lowercase otherwise.

  Args:
    word: The input word.

  Returns:
    The converted word.
  """

  upper_count = 0
  lower_count = 0

  for char in word:
    if 'A' <= char <= 'Z':
      upper_count += 1
    elif 'a' <= char <= 'z':
      lower_count += 1

  if upper_count > lower_count:
    return word.upper()
  else:
    return word.lower()

# Get input
word = input()

# Convert case and print the result
result = convert_case(word)
print(result)
