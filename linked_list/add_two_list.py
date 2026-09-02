
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

def addTwoNumbers( l1: ListNode, l2:ListNode) -> ListNode:

    dummy_n = ListNode(0)
    current = dummy_n
    carry = 0 

    # Fixed: check if l1 and l2 are not None (without .val)
    while l1 is not None or l2 is not None or carry != 0:

        val1 = l1.val if l1 is not None else 0 
        val2 = l2.val if l2 is not None else 0 

        total = val1 + val2 + carry
        carry = total // 10 
        new_digit = total % 10 

        current.next = ListNode(new_digit)
        current = current.next 

        if l1 is not None:
            l1 = l1.next 
        if l2 is not None:
            l2 = l2.next 

    return dummy_n.next

k1 = [1,2,3]
k2 = [4,5,6]

print(addTwoNumbers(k1,k2))