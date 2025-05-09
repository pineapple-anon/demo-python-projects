"""
Start with the root node of the binary tree.
Create an empty queue data structure to perform the breadth-first traversal. Enqueue the root node into the queue.
While the queue is not empty, perform the following steps:
Initialize a variable, level_size, to the current size of the queue (number of nodes in the current level).
Traverse through each node in the current level (equal to level_size):
Dequeue the front node from the queue and call it the current_node.
If i (current index in the level) is less than level_size - 1, set the next pointer of current_node to the first node in the queue (front of the queue) representing the next node at the same level.
Enqueue the left and right children of current_node (if they exist) into the queue.
Return the root node of the modified binary tree with the connections between nodes using the next pointers.
"""

from collections import deque

# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = None  # Pointer to the next node at the same level
# This function connects all nodes at the same level in a binary tree
# using a breadth-first traversal approach.
# It uses a queue to keep track of nodes at the current level and connects
# them to their next right node.
# The function returns the root node of the modified binary tree.
# The time complexity of this function is O(n), where n is the number of nodes in the tree,
# as each node is processed once. The space complexity is O(w), where w is the maximum width of the tree,
# which is the maximum number of nodes at any level in the tree.
# This is typically O(n) in the worst case for a complete binary tree.
# The function uses a queue to perform a level-order traversal of the tree,
# connecting nodes at the same level using their next pointers.
# The function assumes that the binary tree is a perfect binary tree,
# meaning all levels are fully filled except possibly for the last level,
# which is filled from left to right.
def connect(root):
    if not root:
        return None

    queue = deque([root])  # Initialize the queue with the root node

    while queue:
        level_size = len(queue)  # Number of nodes at the current level

        for i in range(level_size):
            current_node = queue.popleft()  # Dequeue the front node

            # Connect to the next node in the same level
            if i < level_size - 1:
                current_node.next = queue[0]  # Set next pointer to the first node in the queue

            # Enqueue left and right children of the current node
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

    return root
        