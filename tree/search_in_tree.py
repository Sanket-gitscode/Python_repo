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



def search_tree(root,target):
    
    
    if root is None:
        return False
    
    if root.data == target:
        return True
    
    
    left_found = search_tree(root.left, target)
    right_found = search_tree(root.right, target)

    return left_found or right_found
    
print(search_tree(root,5))
    
    
    