def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    i = 0
    
    while i < len(heights):
        # If stack is empty or current height is >= height at stack top, push to stack
        if not stack or heights[i] >= heights[stack[-1]]:
            stack.append(i)
            i += 1
        # If current height is < height at stack top, calculate area
        else:
            top = stack.pop()
            
            # Calculate width properly
            # If stack is empty, width is i
            # Otherwise, width is (i - stack[-1] - 1)
            width = i if not stack else (i - stack[-1] - 1)
            area = heights[top] * width
            max_area = max(max_area, area)
    
    # Process remaining bars in the stack
    while stack:
        top = stack.pop()
        
        width = i if not stack else (i - stack[-1] - 1)
        area = heights[top] * width
        max_area = max(max_area, area)
    
    return max_area

# Example usage
if __name__ == "__main__":
    heights = [2, 1, 5, 6, 2, 3]
    print(largest_rectangle_area(heights))  # Output: 10
