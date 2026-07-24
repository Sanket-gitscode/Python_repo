def diagonal_sum_singlepass(array):
    
    n = len(array)
    total = 0 
    
    for i in range(n):
        total += array[i][i]
    
    print(total)


def diagonal_sum_twopass(array):
    
    rows = len(array)
    column = len(array[0])

    total = 0 
    
    for r in range(rows):
        for c in range(column):
            if r == c :
                total += array[r][c]

    print(total)


matrix = [
    [10, 20, 30],  # matrix[0][0] = 10
    [40, 50, 60],  # matrix[1][1] = 50
    [70, 80, 90]   # matrix[2][2] = 90
]

diagonal_sum_singlepass(matrix)
diagonal_sum_twopass(matrix)
