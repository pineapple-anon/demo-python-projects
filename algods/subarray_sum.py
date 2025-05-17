def subarray_sum(arr: list[int], target: int) -> list[int]:
    # prefix_sum 0 happens when we have an empty array
    prefix_sums = {0: 0}
    cur_sum = 0
    for i in range(len(arr)):
        cur_sum += arr[i]
        complement = cur_sum - target
        if complement in prefix_sums:
            return [prefix_sums[complement], i + 1]
        prefix_sums[cur_sum] = i + 1
    return []

# Example usage
if __name__ == "__main__":
    # arr = [1, 2, 3, 7, 5]
    # target = 12
    # result = subarray_sum(arr, target)
    # if result:
    #     print(f"Subarray with sum {target} found between indices {result[0]} and {result[1] - 1}.")
    # else:
    #     print(f"No subarray with sum {target} found.")
    arr = [1, -20, -3, 30, 5, 4]
    target = 7
    result = subarray_sum(arr, target)
    if result:
        print(f"Subarray with sum {target} found between indices {result[0]} and {result[1] - 1}.")
    else:
        print(f"No subarray with sum {target} found.")