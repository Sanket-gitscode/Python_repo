def is_palindrome(text : str)  -> bool :
    
    if len(text) == 0:
        return True
    
    left = 0 
    right = len(text) -1     
    
    while left < right:
        if text[left] != text[right]:
            return False
        
        left += 1 
        right -= 1 
    
    return True
    
#Test case 01 
print(is_palindrome("madam"))      # True


def is_palindrome_robust(text):
    
    cleaned = ''
    
    for ch in text:
        if ch.isalnum():
            cleaned += ch.lower()
            
    left = 0
    right = len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False

        left += 1
        right -= 1

    return True    

#Test cases 02 for robust one 
print(is_palindrome_robust("A man, a plan, a canal: Panama")) # -> True