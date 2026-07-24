def transpose(matrix: list[list[int]]) -> list[list[int]]:
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create a new empty matrix with dimensions (cols x rows)
    result = [[0] * rows for _ in range(cols)]
    
    for r in range(rows):
        for c in range(cols):
            # Swap index positions: r,c becomes c,r!
            result[c][r] = matrix[r][c]
            
    return result

# Test
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(transpose(matrix))
# Output: [[1, 4], [2, 5], [3, 6]]