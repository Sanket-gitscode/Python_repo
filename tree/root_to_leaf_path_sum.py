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


def path_sum(root,target):
    
    if root is None:
        return False
    
    remaining = target - root.data
    
    if root.left is None and root.right is None:
        return remaining == 0

    return path_sum(root.left, remaining) or path_sum(root.right, remaining)
    
    
    
target = 11
print(path_sum(root,target))