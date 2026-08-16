'''
        5
       / \
      4   8
     /   / \
    2   6   10

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create the tree
root = Node(5)

root.left = Node(4)
root.right = Node(8)

root.left.left = Node(2)

root.right.left = Node(6)
root.right.right = Node(10)



def path_sum(root, target):

    if root is None:
        return 0
    
    remaining = target - root.data
    
    if (root.left is None and root.right is None):
        if remaining == 0 :
            return 1 
        else:
            return 0 
        
    
    left_stree = path_sum(root.left,remaining)
    right_stree = path_sum(root.right,remaining)
    
    return left_stree + right_stree 

print(path_sum(root,11))
    