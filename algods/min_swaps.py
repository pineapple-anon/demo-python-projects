def min_swaps(arr):
    n = len(arr)
    
    # Store current indices of elements
    position = {}
    for i in range(n):
        position[arr[i]] = i
    
    visited = [False] * n
    swaps = 0
    
    for i in range(n):
        # If element is already visited or already in correct position
        if visited[i] or arr[i] == i + 1:
            continue
        
        # Find cycle size
        cycle_size = 0
        j = i
        
        while not visited[j]:
            visited[j] = True
            cycle_size += 1
            
            # Move to the next element in the cycle
            # The element at position j should be j+1
            # So find where j+1 currently is
            j = position[j + 1]
        
        # For a cycle of size k, we need k-1 swaps
        swaps += (cycle_size - 1)
    
    return swaps
# Example usage
if __name__ == "__main__":
    arr = [3, 1, 5, 4, 2]
    print(min_swaps(arr))  # Output: 2
# This code defines a function to calculate the minimum number of swaps required to sort an array.