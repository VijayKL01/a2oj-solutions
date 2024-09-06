def max_profit(n, arr):
  """Calculates the maximum profit from a series of transactions.

  Args:
    n: The number of transactions.
    arr: The array of transactions, where each element is the difference between the buying and selling price.

  Returns:
    The maximum profit.
  """

  max_profit = 0
  current_profit = 0

  for i in range(n):
    current_profit += arr[i]
    max_profit = max(max_profit, current_profit)
    if current_profit < 0:
      current_profit = 0

  return max_profit

if __name__ == "__main__":
  n = int(input())
  arr = []

  for _ in range(n):
    a, b = map(int, input().split())
    arr.append(b - a)

  result = max_profit(n, arr)
  print(result)
