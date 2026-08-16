# left  root  right

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create the tree
root = Node(8)

root.left = Node(3)
root.right = Node(10)

root.left.left = Node(1)
root.left.right = Node(6)

root.right.right = Node(14)

root.left.right.left = Node(4)
root.left.right.right = Node(7)


def search_bst(root, target):
    
    if root is None:
        return False
    
    if root.data == target:
        return True 
    
    if target < root.data:
        return search_bst(root.left,target)
    else:
        return search_bst(root.right,target)
    


print(search_bst(root,7))