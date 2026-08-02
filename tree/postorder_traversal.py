#The tree 
'''
    1
   / \
  2   3
 / \
4   5 

'''
#Left -> Right -> ROOT/NODE

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


def postorder_traversal(root):
    
    if root is None:
        return
    
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.data, end =' ')
    
postorder_traversal(root)