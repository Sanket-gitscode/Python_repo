def spiral_matrix(array):
    
    result = []
    
    top = 0 
    bottom = len(array) -1 
    left = 0 
    right = len(array[0]) -1

    while top <= bottom and left <= right:
        
        for col in range(left,right+1):
            result.append(array[top][col])
        
        top += 1 

        for row in range(top,bottom +1):
            result.append(array[row][right])
    
        right -= 1 
        
        for col in range(right,left-1,-1):
            result.append(array[bottom][col])
            
        bottom -= 1
        
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(array[row][left])
            left += 1

    return result

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(spiral_matrix(matrix))



