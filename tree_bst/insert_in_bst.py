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


def insert_bst(root,value):
    
    if root is None:
        return Node(value)
    
    if value < root.data:
        root.left = insert_bst(root.left,value)
    else:
        root.right = insert_bst(root.right,value)
    
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


insert_bst(root, 5)
inorder(root)