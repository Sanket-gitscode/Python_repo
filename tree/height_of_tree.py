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

def height_of_tree(root):
    
    if root is None:
        return -1 
    
    left_subtree_height = height_of_tree(root.left)
    right_subtree_height = height_of_tree(root.right)
    
    return max(left_subtree_height,right_subtree_height) + 1


print(height_of_tree(root))