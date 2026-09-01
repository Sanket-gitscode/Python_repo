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

def pascal_traingle2( rowIndex: int):     # bad solution but works as we build the whole traingle and then reuturn it bad approach
        
        triangle = []

        for i in range(rowIndex):
            if i == 0 :
                triangle.append([1])
            else:
                previous = triangle[-1]
                current = [1]
                
                for j in range(1,len(previous)):
                    current.append(previous[j-1]+previous[j])
                
                current.append(1)
                triangle.append(current)
                
        return triangle[rowIndex]
    
    
def pascal_traingle2_better(rowIndex: int):
    row = [1]

    for i in range(1,rowIndex+1):
      
        row.append(1)

        for j in range(i-1,0,-1):
            row[j] = row[j-1] + row[j]

    return row

print(pascal_traingle2_better(3))
