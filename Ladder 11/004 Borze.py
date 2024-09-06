def convert_to_morse_code(s):
  """Converts a given string to Morse code.

  Args:
    s: The input string.

  Returns:
    The Morse code representation of the string.
  """

  morse_code = ""
  for char in s:
    if char == '.':
      morse_code += "0"
    elif char == '-' and s[i + 1] == '.':
      morse_code += "1"
      i += 1
    elif char == '-' and s[i + 1] == '-':
      morse_code += "2"
      i += 1

  return morse_code

# Get input
s = input()

# Convert to Morse code and print the result
result = convert_to_morse_code(s)
print(result)
