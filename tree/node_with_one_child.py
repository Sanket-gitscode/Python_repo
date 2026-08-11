#The tree 
'''
        1
       / \
      2   3
     /
    4

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

def one_child(root):
    
    if root is None:
        return 0 
    
    if (root.left is not None and root.right is None) or (root.right is not None and root.left is None):
        return 1 + one_child(root.left) + one_child(root.right)
    
    return one_child(root.left) + one_child(root.right)


print(one_child(root))