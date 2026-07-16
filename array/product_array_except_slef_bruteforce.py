def product_array(array : list[int]):
    result = []
    n = len(array)
    
    for i in range(n):
        product = 1 
        for j in range(n):
            if i != j :
                product *= array[j]
                
        result.append(product)
    
    return result 

#Test case 01 
arr = [1,2,3,4]
print(product_array(arr))