def validate_brackets(s: str) -> bool:
    """
    Validate if the brackets in the string are balanced.

    Args:
        s (str): The input string containing brackets.

    Returns:
        bool: True if the brackets are balanced, False otherwise.
    """
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    open_brackets = bracket_map.values()

    for char in s:
        if char in open_brackets:
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack.pop() != bracket_map[char]:
                return False
        else:
            # Ignore non-bracket characters
            continue
    # If stack is empty, all brackets are balanced

    return len(stack) == 0

# Example usage
if __name__ == "__main__":
    test_string = "{[()()]}"
    print(f"Is the string '{test_string}' valid? {validate_brackets(test_string)}")
    test_string = "{[(])}"
    print(f"Is the string '{test_string}' valid? {validate_brackets(test_string)}")
    test_string = "{a{b[1[23(()7)c]]8d}99}"
    print(f"Is the string '{test_string}' valid? {validate_brackets(test_string)}")