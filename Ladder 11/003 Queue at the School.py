def convert_to_python(n, t, word):
  """Converts a given word with 'B' and 'G' characters to its transformed state after t operations.

  Args:
    n: The length of the word.
    t: The number of operations to perform.
    word: The input word.

  Returns:
    The transformed word.
  """

  for _ in range(t):
    for i in range(n - 1):
      if word[i] == 'B' and word[i + 1] == 'G':
        word[i], word[i + 1] = word[i + 1], word[i]

  return word

# Get input
n, t = map(int, input().split())
word = input()

# Convert to Python and print the result
result = convert_to_python(n, t, list(word))
print(''.join(result))
