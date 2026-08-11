from collections import deque

'''
    10
   / \
  5   20
 / \
3   8

'''
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
root = Node(10)  
root.left = Node(5)
root.right = Node(20)

root.left.left = Node(3)
root.left.right = Node(8)



def max_val_intree(root):
    
    if root is None:
        return float('-inf')

    max_left = max_val_intree(root.left)
    max_right = max_val_intree(root.right)
    
    
    return max(max_left,max_right,root.data)

print(max_val_intree(root))