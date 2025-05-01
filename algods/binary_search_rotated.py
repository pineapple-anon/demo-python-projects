def binary_search_rotated(nums, target):
    """
    This function performs a binary search on a rotated sorted array to find the target value.
    :param nums: List[int] - A rotated sorted array
    :param target: int - The target value to search for
    :return: int - The index of the target value in the array, or -1 if not found
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Check if the left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # If the right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
# Example usage
if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    result = binary_search_rotated(nums, target)
    print(f"Index of {target} in the rotated array: {result}")  # Output: Index of 0 in the rotated array: 4

    target = 3
    result = binary_search_rotated(nums, target)
    print(f"Index of {target} in the rotated array: {result}")  # Output: Index of 3 in the rotated array: -1

