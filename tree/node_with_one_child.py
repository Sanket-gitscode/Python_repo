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

    count = 0

    if (root.left is not None and root.right is None) or (root.left is None and root.right is not None):
        count = 1

    return count + one_child(root.left) + one_child(root.right)

print(one_child(root))