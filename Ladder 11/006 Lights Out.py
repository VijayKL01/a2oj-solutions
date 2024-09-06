def check_on(x1, x2, x3=0, x4=0, x5=0):
  """Checks if the sum of the given integers is even.

  Args:
    x1, x2, x3, x4, x5: The integers to check.

  Returns:
    True if the sum is even, False otherwise.
  """

  return (x1 + x2 + x3 + x4 + x5) % 2 == 0

if __name__ == "__main__":
  a11, a12, a13 = map(int, input().split())
  a21, a22, a23 = map(int, input().split())
  a31, a32, a33 = map(int, input().split())

  print(check_on(a11, a12, a21), check_on(a11, a12, a13, a22), check_on(a13, a12, a23), sep="")
  print(check_on(a21, a22, a11, a31), check_on(a22, a21, a12, a23, a32), check_on(a23, a22, a13, a33), sep="")
  print(check_on(a31, a21, a32), check_on(a32, a22, a31, a33), check_on(a33, a32, a23), sep="")
