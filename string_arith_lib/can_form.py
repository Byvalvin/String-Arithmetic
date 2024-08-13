from collections import Counter

def can_form_string(left, right, allow_repeats=False):
    """
    Check if the `right` string can be formed using letters from the `left` string.

    Parameters:
    - left: The string containing the letters to use.
    - right: The string that needs to be formed.
    - allow_repeats: If True, allows repeating characters from `left` in `right`.

    Returns:
    - True if `right` can be formed from `left` with the given constraints, False otherwise.
    """
    # Create frequency counters for both strings
    left_count = Counter(left)
    right_count = Counter(right)
    
    if allow_repeats:
        # If repeats are allowed, check if left has enough distinct characters
        for char in right_count:
            if char not in left_count:
                return False
        return True
    
    # If repeats are not allowed, check if left contains enough of each character
    for char in right_count:
        if left_count[char] < right_count[char]:
            return False

    return True
