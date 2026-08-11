#The tree 
'''
    1
   / \
  2   3
 / \
4   5 

'''
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
root = Node(1)  
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

def two_child(root):
    
    if root is None:
        return 0 
    
    count = 0 
    
    if root.left and root.right:
        count += 1 
    
    return count + two_child(root.left) + two_child(root.right)
    

print(two_child(root))