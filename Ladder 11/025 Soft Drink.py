def calculate_minimum_ingredients(n, k, l, c, d, p, nl, np):
  """Calculates the minimum number of ingredients required for a recipe.

  Args:
    n: The number of servings required.
    k: The number of bottles of milk.
    l: The number of loaves of bread.
    c: The number of packets of sugar.
    d: The number of packets of flour.
    p: The number of packets of salt.
    nl: The number of servings per bottle of milk.
    np: The number of servings per packet of salt.

  Returns:
    The minimum number of ingredients required.
  """

  tp = (k * l // nl) // n
  lp = (d * c) // n
  sp = (p // np) // n

  return min(tp, lp, sp)

if __name__ == "__main__":
  n, k, l, c, d, p, nl, np = map(int, input().split())

  result = calculate_minimum_ingredients(n, k, l, c, d, p, nl, np)
  print(result)
