class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        map_s_to_t = {}
        map_t_to_s = {}
        
        for c1, c2 in zip(s, t):
            # Check if c1 is already mapped to a different character
            if c1 in map_s_to_t and map_s_to_t[c1] != c2:
                return False
            # Check if c2 is already mapped from a different character
            if c2 in map_t_to_s and map_t_to_s[c2] != c1:
                return False
                
            # Save the mapping
            map_s_to_t[c1] = c2
            map_t_to_s[c2] = c1
            
        return True

# --- Example Usage ---
solver = Solution()

# Example 1: True (e -> a, g -> d)
print(solver.isIsomorphic("egg", "add")) 
# Output: True

# Example 2: False ('o' maps to both 'a' and 'r')
print(solver.isIsomorphic("foo", "bar")) 
# Output: False

# Example 3: True (p -> t, a -> i, p -> t, e -> l, r -> e)
print(solver.isIsomorphic("paper", "title")) 
# Output: True