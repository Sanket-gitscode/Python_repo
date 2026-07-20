def revrese_word( string : str):
    
    worldlist = string.split()
    
    left = 0 
    right = len(worldlist) -1
    
    while left < right :
        worldlist[left],worldlist[right] = worldlist[right], worldlist[left]
        left += 1
        right -= 1
        
    
    return ' '.join(worldlist)


s = 'Hello world'
print(revrese_word(s))