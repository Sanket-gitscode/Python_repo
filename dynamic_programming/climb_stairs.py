def climb_stairs(n):
    # Base cases
    if n == 1: 
        return 1
    if n == 2: 
        # You can do 1+1 or 2
        return 2 
    
    # 1. Create a "notebook" (array) to store answers
    # We make it size n+1 so the index matches the step number
    ways = [0] * (n + 1)
    
    # 2. Fill in the base answers we already know
    ways[1] = 1
    ways[2] = 2
    
    # 3. Look back at previous answers to build new ones
    for step in range(3, n + 1):
        ways[step] = ways[step - 1] + ways[step - 2]
        
    # 4. Return the final answer
    return ways[n]

# Example: How many ways to climb 5 stairs?
print(climb_stairs(5)) # Output: 8
