import random

def jumble_string(s):
    """
    Jumble up the letters of a string randomly.

    Parameters:
    - s: The string to jumble.

    Returns:
    - A new string with the letters shuffled randomly.
    """
    if not s:
        return s

    # Convert string to list of characters
    char_list = list(s)
    
    # Shuffle the list in place
    random.shuffle(char_list)
    
    # Join the list back into a string
    return ''.join(char_list)
