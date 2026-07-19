def reverse_a_string(text):
    
    char_list = list(text)
    left = 0
    right = len(char_list) - 1

    while left < right:
        char_list[left], char_list[right] = char_list[right], char_list[left]
        left += 1
        right -= 1

    reversed_text = "".join(char_list)

    return reversed_text


def method_2_reverse(text):
    
    rev_text =  ''
    n = len(text)
    
    for i in range(n-1,-1,-1):
        rev_text += text[i]
        
    return rev_text


#Test case 01 
text = "Hello World"
print(reverse_a_string(text))
print(method_2_reverse(text))
    