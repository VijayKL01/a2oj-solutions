def solve(y, k, n):
  """Finds the smallest integer x such that y + x is divisible by k and x <= n - y.

  Args:
    y: The given integer.
    k: The divisor.
    n: The upper bound.

  Returns:
    The smallest integer x if found, otherwise -1.
  """

  x = k - y % k
  for i in range(x, n - y + 1, k):
    print(i, end=" ")
    return

  print(-1)

if __name__ == "__main__":
  t = 1
  # t = int(input())

  for _ in range(t):
    y, k, n = map(int, input().split())
    solve(y, k, n)
