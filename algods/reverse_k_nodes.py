class Node:
    def __init__(self, data=0, next=None):
        self.data=data
        self.next=next

def reverse_k(head:Node, k:int):
    count=0
    current=head

    while current and count<k:
        current=current.next
        count+=1

    if count<k:
        return head

    count=0
    prev=None
    current=head
    next_node=None

    while current and count<k:
        next_node=current.next
        current.next=prev
        prev=current
        current=next_node
        count+=1
    # 'prev' is now the new head of the reversed group
    # 'curr' is now the first node of the next group
    # 'head' is now the last node of the reversed group

    # Recursively reverse next group and connect

    if next_node:
        head.next=reverse_k(next_node,k)

    return prev
