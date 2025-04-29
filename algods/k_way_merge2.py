"""Kth Smallest Element in a Sorted Matrix"""

def kth_smallest_element(matrix, k):
    """
    Find the kth smallest element in a sorted matrix.
    The matrix is sorted in ascending order both row-wise and column-wise.
    """
    import heapq

    rows = len(matrix)
    cols = len(matrix[0])
    min_heap = []

    # Push the first element of each row into the heap
    for i in range(min(rows, k)):
        heapq.heappush(min_heap, (matrix[i][0], i, 0))

    # Extract the smallest element k times
    for _ in range(k):
        element, row, col = heapq.heappop(min_heap)

        # If there is a next element in the same row, push it into the heap
        if col + 1 < cols:
            heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))

    return element
# Example usage
if __name__ == "__main__":
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    k = 8
    print(f"The {k}th smallest element in the matrix is: {kth_smallest_element(matrix, k)}")
# Output: The 8th smallest element in the matrix is: 13
