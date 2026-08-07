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



def count_nodes(root):
    
    if root is None:
        return 0 
    
    count_left = count_nodes(root.left)
    count_right = count_nodes(root.right)
    
    return count_left + count_right + 1 


print(count_nodes(root))
    
    