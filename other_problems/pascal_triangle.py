def generate(numRows):
    
    traingle = []
    
    
    for i in range(numRows):
        
        
        if i == 0 :
            traingle.append([1])
        else:
            
            previous = traingle[-1]
            current = [1]
            
            for j in range(1,len(previous)):
                 current.append(previous[j-1]+previous[j])
            
            current.append(1)
                       
            traingle.append(current)

    return traingle


print(generate(5))