"""
**Instruction**
Please see instruction document.

"""
from linked_list_helper import ListNode
def P4(head: ListNode) -> ListNode: 
    first = None
    while head:
        last = head.next
        head.next = first
        first = head
        head = last
            
    return first