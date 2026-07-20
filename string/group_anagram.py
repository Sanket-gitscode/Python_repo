def group_anagram(words : list):
    
    group = {}
    
    for word in words:
        
        key = ''.join(sorted(word))
        
        if key not in group:
            group[key] = []
            
        
        group[key].append(word)
        
    return list(group.values())
    
    
words = ["cat", "dog", "tac", "god", "act", "bird"]
print(group_anagram(words))