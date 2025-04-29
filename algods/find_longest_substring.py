
def find_longest_substring(s: str) -> str:
    """
    Find the longest substring without repeating characters in a given string.

    Args:
        s (str): The input string.

    Returns:
        str: The longest substring without repeating characters.
    """
    char_index_map = {}
    start = max_length = 0
    longest_substring = ""

    for i, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        char_index_map[char] = i
        current_length = i - start + 1

        if current_length > max_length:
            max_length = current_length
            longest_substring = s[start:i + 1]

    return longest_substring

# Example usage
input_str = "abcabcbb"
result = find_longest_substring(input_str)
print(f"Input: '{input_str}'")
print(f"Longest substring without repeating characters: '{result}'")
print(f"Length: {len(result)}")