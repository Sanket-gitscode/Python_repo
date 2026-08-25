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


def max_depth_of_tree(root):
    
    if root is None:
        return 0 
    
    left_sub_tree = max_depth_of_tree(root.left)
    right_sub_tree = max_depth_of_tree(root.right)
    
    return 1 + max(left_sub_tree,right_sub_tree) #we add 1 for node itself and we use max for tree with maxdepth
    
    
    
print(max_depth_of_tree(root))