def find_first_occurence(arr, target):
    """
    Find the first occurrence of a target value in a sorted array.

    Args:
        arr (list): A sorted list of integers.
        target (int): The target value to find.

    Returns:
        int: The index of the first occurrence of the target value, or -1 if not found.
    """
    n=len(arr)
    left,right=0,n-1
    bound_idx=-1
    
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target: # feasible condition
            bound_idx=mid
            right=mid-1
        elif arr[mid]<target:
            left=mid+1 
        else:
            left=mid+1
    return bound_idx

# Example usage
if __name__ == "__main__":
    arr = [4, 6, 7, 7, 7, 20]
    target = 5
    result = find_first_occurence(arr, target)
    if result != -1:
        print(f"The first occurrence of {target} is at index {result}.")
    else:
        print(f"{target} not found in the array.")
    target = 7
    result = find_first_occurence(arr, target)
    if result != -1:
        print(f"The first occurrence of {target} is at index {result}.")
    else:
        print(f"{target} not found in the array.")