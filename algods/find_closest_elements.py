def find_closest_elements(nums, k , target):
    """
    Find the k closest elements to the target in a sorted array.
    :param nums: List[int] - A sorted array
    :param k: int - The number of closest elements to find
    :param target: int - The target value
    :return: List[int] - The k closest elements to the target
    """
    # Edge case: if array length equals k, return the entire array
    if len(nums) == k:
        return nums
    
    # Find the position where target would be inserted
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    # Now left is the insertion point
    # Initialize two pointers around this position
    left = right  # right already points to the element <= target
    right = left + 1  # left + 1 points to the element > target
    
    # Expand window to find k closest elements
    result = []
    while k > 0:
        # If we've exhausted elements on the right or
        # if left element is valid and closer to target than right
        if right >= len(nums) or (left >= 0 and 
           abs(nums[left] - target) <= abs(nums[right] - target)):
            result.append(nums[left])
            left -= 1
        else:
            result.append(nums[right])
            right += 1
        k -= 1
    
    # Sort the result array
    result.sort()

    return result

# Example usage
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    k = 4
    target = 3
    print(f"The {k} closest elements to {target} are: {find_closest_elements(nums, k, target)}")
# Output: The 4 closest elements to 3 are: [1, 2, 3, 4]