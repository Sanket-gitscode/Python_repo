def lengthOfLastWord(s: str) -> int:

    length_word = 0
    index = len(s) - 1 

    while index >=0 and s[index] == ' ':
        index -= 1 
    
    while index >= 0 and s[index] != ' ':
        length_word += 1 
        index -= 1 
    
    return length_word


def lengthOfLastWord2(self, s: str) -> int:

    wordlist = s.split()
    last_word = wordlist[-1]

    return len(last_word)

#Test case 01 
text = "Hello world"
print(lengthOfLastWord(text))