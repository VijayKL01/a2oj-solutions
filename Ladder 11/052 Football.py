def find_longest_substring(s):
  

  count = 1
  max_count = 1

  for i in range(1, len(s)):
    if s[i] == s[i - 1]:
      count += 1
      max_count = max(max_count, count)
    else:
      count = 1

  return max_count

if __name__ == "__main__":
  s = input()

  result = find_longest_substring(s)
  print("YES" if result >= 7 else "NO")
