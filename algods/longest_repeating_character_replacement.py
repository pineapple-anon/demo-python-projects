def longest_repeating_character_replacement(s, k):
    """
    Find the length of the longest substring that can be obtained by replacing at most k characters in the string s.

    Args:
        s (str): The input string.
        k (int): The maximum number of characters that can be replaced.

    Returns:
        int: The length of the longest substring after replacements.
    """
    # Initialize a dictionary to keep count of characters in current window
    char_count = {}
    
    # Variables to track window and result
    left = 0
    max_length = 0
    max_count = 0  # Track the most frequent character count
    
    for right in range(len(s)):
        # Add current character to count
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        # Update the max_count (most frequent character in current window)
        max_count = max(max_count, char_count[s[right]])
        
        # KEY INSIGHT
        # If current window size - count of most frequent character > k,
        # we need to shrink the window from the left
        if (right - left + 1) - max_count > k:
            char_count[s[left]] -= 1
            left += 1
        
        # Update max length found so far
        max_length = max(max_length, right - left + 1)
    
    return max_length