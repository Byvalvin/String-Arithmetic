def string_division(left, right):
    """
    Perform string division or find substrings repeating `n` times based on the type of `right`.
    
    - If `right` is a string:
        - If `right` is smaller than or equal to `left`, count how many times `right` appears as a contiguous substring in `left` and compute the remainder.
        - If `right` is larger than `left`, return the fraction of how much `right` fits into `left` and the remainder of `right` after subtracting the portion that fits.
    - If `right` is an integer `n`, return substrings of `left` of length up to `n` that repeat exactly `n` times.

    Parameters:
    - left: The string to be divided or analyzed.
    - right: Either the string to divide by or an integer specifying the number of repetitions.

    Returns:
    - A tuple:
      - If `right` is a string:
        - (fraction, remainder) where fraction is the number of times `right` appears in `left` if `right` is smaller or equal.
        - (fraction, remainder) where fraction is the fraction of how much `right` fits into `left` if `right` is larger.
      - If `right` is an integer `n`:
        - A tuple (substrings, left) where substrings is a list of substrings of length up to `n` that repeat exactly `n` times.
    """
    
    # Handle case where `right` is an integer
    if isinstance(right, int):
        if right <= 0:
            raise ValueError("The repetition count must be a positive integer.")
        
        len_left = len(left)
        repeating_substrings = set()

        # Check all possible lengths of substrings from 1 to `right`
        for length in range(1, right + 1):
            for i in range(len_left - length + 1):
                substring = left[i:i + length]
                # Check if this substring repeats exactly `n` times
                if left.count(substring) == right:
                    repeating_substrings.add(substring)
        
        # Return the sorted list of repeating substrings and the original `left`
        return sorted(repeating_substrings), left

    # Handle case where `right` is a string
    if isinstance(right, str):
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

    raise TypeError("The `right` parameter must be either a string or an integer.")
