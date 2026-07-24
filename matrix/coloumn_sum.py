def column_sum(array: list[list[int]]):
    rows = len(array)
    cols = len(array[0])
    
    # Outer loop picks the column (Col 0, then Col 1, then Col 2)
    for c in range(cols):
        col_sum = 0
        # Inner loop steps down through every row
        for r in range(rows):
            col_sum += array[r][c]  # Notice r changes while c stays constant!
        print(f"Col {c} Sum: {col_sum}")

matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

column_sum(matrix)