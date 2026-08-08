'''
    1
   / \
  2   3
 / \
4   5 

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
root.left.right = Node(5)



def sum_of_nodes(root):
    
    if root is None:
        return 0 
    
    left_sum = sum_of_nodes(root.left)
    right_sum = sum_of_nodes(root.right)
    
    return left_sum + right_sum + root.data



print(sum_of_nodes(root))
    