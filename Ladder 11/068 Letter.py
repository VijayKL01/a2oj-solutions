def check_anagrams(s1, s2):
 
  if len(s1) != len(s2):
    return "NO"

  count = [0] * 256
  for char in s1:
    count[ord(char)] += 1

  for char in s2:
    if char != ' ':
      count[ord(char)] -= 1
      if count[ord(char)] < 0:
        return "NO"

  return "YES"

if __name__ == "__main__":
  t = int(input())

  for _ in range(t):
    s1 = input()
    s2 = input()

    result = check_anagrams(s1, s2)
    print(result)
