def checkInclusion( string1 : str, string2: str):
    
    if len(string1) > len(string2):
        return False
    
    
    left = 0 
    needed = [0] * 26
    window = [0] * 26 
    
    for ch in string1:
        needed[ord(ch)- ord('a')] += 1
    
    
    for right in range(len(string2)):
        
        window[ord(string2[right]) - ord('a')] +=1 
    
        if right - left + 1 > len(string1):
            window[ord(string2[left]) - ord('a')] -= 1
            left += 1 
        
        if window == needed:
            return True 
    
    return False


print(checkInclusion("ab", "eidbhaooo"))