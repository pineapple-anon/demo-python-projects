class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_list(head):
    """
    Reverses a singly linked list.

    :param head: The head of the linked list.
    :return: The new head of the reversed linked list.
    """
    prev = None
    current = head

    while current:
        next_node = current.next  # Store the next node
        current.next = prev       # Reverse the link
        prev = current            # Move prev to current
        current = next_node       # Move to the next node

    return prev  # New head of the reversed list

# Test the reverse_list function
# Example usage
if __name__ == "__main__":
    # Creating a linked list: 1 -> 2 -> 3 -> 4
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    # Reversing the linked list
    new_head = reverse_list(head)

    # Printing the reversed linked list
    current = new_head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")
# Output: 4 -> 3 -> 2 -> 1 -> None