from binary_search import binary_search

def find_closest_elements(nums, k, target):
    if len(nums) == k:
        return nums

    if target <= nums[0]:
        return nums[0:k]
        
    if target >= nums[-1]:
        return nums[len(nums)-k : len(nums)]

    first_closest = binary_search(nums, target)

    window_left = first_closest - 1
    window_right = window_left + 1

    while (window_right - window_left - 1) < k:
        if window_left == -1:
            window_right += 1
            continue

        if window_right == len(nums) or abs(nums[window_left] - target) <= abs(nums[window_right] - target):
            window_left -= 1
        
        else:
            window_right += 1

    return nums[window_left + 1 : window_right]

# Driver code
def main():

    nums = [
                [1, 2, 3, 5, 6, 7,8],
                [1, 2, 3, 4, 5],
                [1, 2, 4, 5, 6],
                [1, 2, 3, 4, 5, 10]
                ]
    k = [4, 4, 2, 3]
    num = [4, 3, 10, -5]
    for i in range(len(nums)):
        print((i + 1), ".\tThe ", k[i],
              " Closest Elements for the number ", num[i], " in the array ",
              nums[i], " are:", sep="")
        print("\t", find_closest_elements(nums[i], k[i], num[i]))
        print("-" * 100)

if __name__ == '__main__':
    main()