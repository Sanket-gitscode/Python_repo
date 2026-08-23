def range_query_sum(array : list[int] , query_array : list[int]):
    
    for query in query_array:
        left , right = query

        sum = 0 
        
        for i in range(left,right + 1):
            sum += array[i]
        
        print(f" Query is {query}, left = {left}, right= {right}, sum_query = {sum}")



# Input array
arr = [1, 1, 2, 1, 3, 4, 5, 2, 8]
# Query ranges
queries = [[0, 4], [1, 3], [2, 4]]

(range_query_sum(arr,queries))