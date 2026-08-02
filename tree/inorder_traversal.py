#The tree 
'''
    1
   / \
  2   3
 / \
4   5 

'''


#Left → ROOT/NODE → Right

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


def inorder_traversal(root):
    
    if root is None:
        return
    
    inorder_traversal(root.left)
    print(root.data, end =' ')
    inorder_traversal(root.right)
    
inorder_traversal(root)