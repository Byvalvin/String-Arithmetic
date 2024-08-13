def string_subtraction(left, right):
    """
    Perform string subtraction based on the given rules:
    
    - Case 1: If `right` is smaller and found in `left`, remove it once.
    - Case 2: If `right` is not found in `left`, return `left`.
    - Case 3: If `right` is larger and `left` is found in `right`, remove `left` and flip the rest of `right`.
    - Case 4: If `right` is larger and `left` is not found in `right`, return `left`.

    Parameters:
    - left: The string from which to subtract.
    - right: The string to subtract.

    Returns:
    - The resulting string after performing the subtraction.
    """
    
    # Case 1: If right is smaller and found in left, remove it once
    if len(right) <= len(left) and right in left:
        return left.replace(right, '', 1)
    
    # Case 2: If right is not found in left, return left
    if len(right) <= len(left) and right not in left:
        return left
    
    # Case 3: If right is larger and left is found in right
    if len(right) > len(left):
        if left in right:
            # Remove the first occurrence of left from right
            right_removed = right.replace(left, '', 1)
            # Flip the remaining part of right
            return right_removed[::-1]
    
    # Case 4: If right is larger and left is not found in right
    if len(right) > len(left) and left not in right:
        return left
