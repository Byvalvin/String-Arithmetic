def string_division(left, right):
    """
    Perform string division based on the given rules:
    
    - If `right` is smaller than or equal to `left`, count how many times `right` appears as a contiguous substring in `left` and compute the remainder.
    - If `right` is larger than `left`, return the fraction of how much `right` fits into `left` and the remainder of `right` after subtracting the portion that fits.

    Parameters:
    - left: The string to be divided.
    - right: The string to divide by.

    Returns:
    - A tuple (fraction, remainder) where:
      - fraction: The number of times `right` appears in `left` if `right` is smaller or equal.
      - fraction: The fraction of how much `right` fits into `left` if `right` is larger.
      - remainder: The remainder string after division.
    """
    
    # Handle edge case where the right string is empty
    if not right:
        raise ValueError("Cannot divide by an empty string.")

    len_left = len(left)
    len_right = len(right)

    if len_right <= len_left:
        # Count the number of non-overlapping occurrences of `right` in `left`
        count = 0
        remainder = left
        while right in remainder:
            count += 1
            remainder = remainder.replace(right, '', 1)
        
        return count, remainder

    else:
        # Calculate the fraction and remainder if `right` is larger than `left`
        if len_right > 0 and len_left > 0:
            fraction = len_left / len_right
            remainder = right[len_left:]  # The part of `right` that doesn't fit
            return fraction, remainder
        
        return 0, left  # Return 0 and the original left if right cannot fit into left
