#The traversal tells us where to go. The "visit" tells us what to do when we get there.

# PREORDER  ->   ROOT/NODE -> Left -> Right

#Test tree

'''   
    1
   / \
  2   3
 / \
4   5 

'''
#Tree Node

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


# tree elemenets 

root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)



def preorder_traversal(root):
    
    if root is None:
        return
    
    print(root.data, end = ' ')

    preorder_traversal(root.left)
    
    preorder_traversal(root.right)
    

preorder_traversal(root)