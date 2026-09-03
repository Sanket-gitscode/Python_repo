def single_numner(array : list[int]) -> int:
    
    num_map = {}
    
    for num in array:
        num_map[num] = num_map.get(num, 0) + 1
        
    
    for key,value in num_map.items():
        if num_map[key] == 1:
            return key




#test array 1 
arr = [4,1,2,1,2]
print(single_numner(arr))