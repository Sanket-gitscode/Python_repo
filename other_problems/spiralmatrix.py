def spiral_matrix(matrix):
    
    result = []

    left = 0
    right = len(matrix[0]) - 1
    top = 0
    bottom = len(matrix) - 1

    while left <= right and top <= bottom:

        # left -> right
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # top -> bottom
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        # right -> left
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        # bottom -> top
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(spiral_matrix(matrix))



