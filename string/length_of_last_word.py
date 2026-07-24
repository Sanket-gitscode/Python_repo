def length_of_last_word(string : str):
    
    length = 0 
    idx = len(string) - 1
    
    
    while idx >= 0 and string[idx] == ' ':
            idx -= 1
    
    while idx >= 0 and string[idx] != ' ' :
        length += 1 
        idx -= 1 
    
    return length

def lengthOfLastWord2(self, s: str) -> int:

    wordlist = s.split()
    last_word = wordlist[-1]

    return len(last_word)

#Test case 01 
text = "Hello world"
print(length_of_last_word(text))