# 1d list 
def row_of_matrix():
    row = [10, 20, 30]


#2d
matrix = [
    [10, 20, 30],  # Row 0
    [40, 50, 60],  # Row 1
    [70, 80, 90]   # Row 2
]

matrix = [
    [10, 20, 30],  # Row 0
    [40, 50, 60],  # Row 1
    [70, 80, 90]   # Row 2
]

def matrix1(array):
    rows = len(array)        # 3
    cols = len(array[0])     # 3

    # Loop through row indices: 0, 1, 2
    for r in range(rows):
        # Loop through col indices: 0, 1, 2
        for c in range(cols):
            print(f"Row {r}, Col {c} -> {array[r][c]}")

matrix1(matrix)