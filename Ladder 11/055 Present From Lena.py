def print_pattern(n):
 
  for i in range(n + 1):
    print(" " * (n - i), end="")
    for j in range(2 * i + 1):
      if j < i:
        print(j, end=" ")
      elif j == i and i == 0:
        print(i, end="")
      elif j == i:
        print(i, end=" ")
      elif j > i and j != 2 * i:
        print(j - (j - i) * 2, end=" ")
      else:
        print(j - (j - i) * 2, end="")
    print()

  for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    for j in range(2 * i + 1):
      if j < i:
        print(j, end=" ")
      elif j == i and i == 0:
        print(i, end="")
      elif j == i:
        print(i, end=" ")
      elif j > i and j != 2 * i:
        print(j - (j - i) * 2, end=" ")
      else:
        print(j - (j - i) * 2, end="")
    print()

if __name__ == "__main__":
  t = int(input())

  for _ in range(t):
    n = int(input())
    print_pattern(n)
