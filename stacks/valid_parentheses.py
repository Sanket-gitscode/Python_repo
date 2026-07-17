def valid_parantheses(text : str):
    
    stack =[]
    pairs ={
        ')':'(',
        ']':'[',
        '}':'{'
    }
    
    for ch in text:
        if ch in pairs:
            if not stack and stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)
    
    return not stack
    

s ="()[]{}"
print(valid_parantheses(s))