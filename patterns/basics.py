"""Comprehensive Python script containing all essential printing and matrix patterns

frequently tested in coding interviews and foundational DSA practice.
"""


def print_right_triangle(n: int):
  print(f"--- Right-Angled Triangle (n={n}) ---")
  for i in range(1, n + 1):
    print("*" * i)
  print()


def print_pyramid(n: int):
  print(f"--- Pyramid Pattern (n={n}) ---")
  for i in range(n):
    spaces = " " * (n - i - 1)
    stars = "*" * (2 * i + 1)
    print(spaces + stars)
  print()


def print_number_triangle(n: int):
  print(f"--- Number Triangle Pattern (n={n}) ---")
  for i in range(1, n + 1):
    row = "".join(str(j) for j in range(1, i + 1))
    print(row)
  print()


def print_floyds_triangle(n: int):
  print(f"--- Floyd's Triangle (n={n}) ---")
  num = 1
  for i in range(1, n + 1):
    row = []
    for _ in range(i):
      row.append(str(num))
      num += 1
    print(" ".join(row))
  print()


def print_binary_triangle(n: int):
  print(f"--- Binary Triangle (0-1 Triangle) (n={n}) ---")
  for i in range(n):
    row = []
    for j in range(i + 1):
      if (i + j) % 2 == 0:
        row.append("1")
      else:
        row.append("0")
    print(" ".join(row))
  print()


def print_diamond(n: int):
  print(f"--- Diamond Pattern (n={n}) ---")
  # Upper Pyramid
  for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
  # Lower Inverted Pyramid
  for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
  print()


def print_butterfly(n: int):
  print(f"--- Butterfly Pattern (n={n}) ---")
  # Upper half
  for i in range(1, n + 1):
    stars = "*" * i
    spaces = " " * (2 * (n - i))
    print(stars + spaces + stars)
  # Lower half
  for i in range(n, 0, -1):
    stars = "*" * i
    spaces = " " * (2 * (n - i))
    print(stars + spaces + stars)
  print()


def print_spiral_matrix(n: int):
  print(f"--- Spiral Matrix Pattern (n={n}) ---")
  matrix = [[0] * n for _ in range(n)]
  top, bottom = 0, n - 1
  left, right = 0, n - 1
  num = 1

  while top <= bottom and left <= right:
    # Traverse Left to Right
    for i in range(left, right + 1):
      matrix[top][i] = num
      num += 1
    top += 1

    # Traverse Top to Bottom
    for i in range(top, bottom + 1):
      matrix[i][right] = num
      num += 1
    right -= 1

    # Traverse Right to Left
    if top <= bottom:
      for i in range(right, left - 1, -1):
        matrix[bottom][i] = num
        num += 1
      bottom -= 1

    # Traverse Bottom to Top
    if left <= right:
      for i in range(bottom, top - 1, -1):
        matrix[i][left] = num
        num += 1
      left += 1

  for row in matrix:
    print("\t".join(str(x) for x in row))
  print()


if __name__ == "__main__":
  print_right_triangle(4)
  print_pyramid(4)
  print_number_triangle(4)
  print_floyds_triangle(4)
  print_binary_triangle(4)
  print_diamond(3)
  print_butterfly(3)
  print_spiral_matrix(3)