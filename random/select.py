import random

def pick_random_chars(s, n):
    """
    Pick `n` random characters from a given string.

    Parameters:
    - s: The string to pick characters from.
    - n: The number of random characters to pick.

    Returns:
    - A string with `n` random characters picked from the input string.
    """
    if not s:
        return ''
    
    # Ensure `n` is not greater than the length of the string
    n = min(n, len(s))
    
    # Pick `n` random characters from the string
    picked_chars = random.sample(s, n)
    
    # Return the picked characters as a string
    return ''.join(picked_chars)
