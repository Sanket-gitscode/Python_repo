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


def count_leaf_nodes(root):
    
    if root is None:
        return 0 
    
    if root.left is None and root.right is None:
        return 1 
    
    leaf_left = count_leaf_nodes(root.left)
    leaf_right = count_leaf_nodes(root.right)
    
    
    return leaf_left + leaf_right

print(count_leaf_nodes(root))