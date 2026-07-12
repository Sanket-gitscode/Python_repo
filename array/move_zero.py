def move_zero (array:list[int]):
    
    index = 0 
    
    for num in range(len(array)):
        if array[num] != 0 :
            array[num],array[index]= array[index],array[num]
            index += 1
    
    return array
    
    
    
#Test case 01 
test1 = [0, 1, 0, 3, 12]
print(move_zero(test1))