def sum_of_rows(array : list[int]):  # without index 
    
    row = len(array)
    col = len(array[0]) 
    
    for rows in array: # rows become [10,20,30]
        row_sum = 0 
        for col in rows:  # col becomes values in rows 10,20,30 iterating over that row 
            row_sum += col
        print(row_sum)

matrix = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
]

sum_of_rows(matrix)

def sum_of_rows_index(array : list[int]): #with index using range:
    
    row = len(array)
    col = len(array[0])
    
    for rows in range(row):
        row_sum = 0 
        for column in range(col):
            row_sum += array[rows][column]
        print(row_sum)
        
sum_of_rows_index(matrix)