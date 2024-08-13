def rotate_string_custom(s, left_rotations=0, right_rotations=0):
    """
    Rotate a string `s` by specified numbers of left and right rotations.

    Parameters:
    - s: The string to rotate.
    - left_rotations: The number of positions to rotate to the left.
    - right_rotations: The number of positions to rotate to the right.

    Returns:
    - The rotated string.
    """
    if not s:
        return s

    length = len(s)

    # Normalize the number of rotations to be within the bounds of the string length
    left_rotations = left_rotations % length
    right_rotations = right_rotations % length

    # Calculate the effective rotation
    net_rotation = (right_rotations - left_rotations) % length

    # Apply rotation
    return s[-net_rotation:] + s[:-net_rotation] if net_rotation else s

# Example usage:
# print(rotate_string_custom("abcd", left_rotations=1, right_rotations=2))  # Output: "dabc"
