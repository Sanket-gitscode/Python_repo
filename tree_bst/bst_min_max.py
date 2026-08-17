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

root.left.right.left = Node(4)
root.left.right.right = Node(7)

root.left.right.left.right = Node(5)

root.right.right = Node(14)


def min_bst(root):
    
    if root.left is None:
        return root.data
    
    return min_bst(root.left)

print(min_bst(root))


def max_bst(root):
    
    if root.right is None:
        return root.data
    
    return max_bst(root.right)

print(max_bst(root))