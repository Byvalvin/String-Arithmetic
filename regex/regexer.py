import re

def build_regex(digit=False, letter=False, specific_string=None, min_length=0, max_length=None, start_with=None, end_with=None, char_spec=None, allowed_chars=None, disallowed_chars=None, exact_one='1'):
    """
    Build a regex string based on the given specifications including character constraints.

    Parameters:
    - digit: If True, include digits in the regex pattern.
    - letter: If True, include letters in the regex pattern.
    - specific_string: A specific string to match exactly.
    - min_length: Minimum length of the string to match.
    - max_length: Maximum length of the string to match.
    - start_with: String that the match must start with.
    - end_with: String that the match must end with.
    - char_spec: A dictionary where keys are characters and values are tuples specifying constraints.
    - allowed_chars: A list of characters that are allowed in the match.
    - disallowed_chars: A list of characters that are disallowed in the match.
    - exact_one: Character that must appear exactly once. If None, no such requirement.

    Returns:
    - A regex pattern string that matches the given specifications.
    """
    
    if char_spec is None:
        char_spec = {}

    if allowed_chars is None:
        allowed_chars = []

    if disallowed_chars is None:
        disallowed_chars = []

    # Base character set pattern
    char_patterns = []

    if digit:
        char_patterns.append(r'\d')
    if letter:
        char_patterns.append(r'[a-zA-Z]')

    if allowed_chars:
        char_patterns.append(f'[{"".join(re.escape(c) for c in allowed_chars)}]')
    else:
        if digit:
            char_patterns.append(r'\d')
        if letter:
            char_patterns.append(r'[a-zA-Z]')
        if char_patterns:
            char_patterns.append(f'[{"".join(char_patterns)}]')
        else:
            char_patterns.append(f'[]')

    # Add specific character constraints
    for char, (x, orless, ormore) in char_spec.items():
        if orless and ormore:
            raise ValueError("Character cannot be both 'orless' and 'ormore'.")
        
        if orless:
            char_patterns.append(f'{re.escape(char)}{{0,{x}}}')
        elif ormore:
            char_patterns.append(f'{re.escape(char)}{{{x},}}')
        else:
            char_patterns.append(f'{re.escape(char)}{{{x}}}')
    
    if disallowed_chars:
        # Disallow certain characters
        disallowed_pattern = ''.join(re.escape(c) for c in disallowed_chars)
        char_patterns.append(f'[^{disallowed_pattern}]')

    combined_chars = ''.join(char_patterns)
    
    # Handle exact one requirement
    if exact_one:
        pattern = f'^0*{re.escape(exact_one)}0*$'
    else:
        if min_length > 0 or max_length is not None:
            length_pattern = ''
            if min_length > 0:
                length_pattern += f'{{{min_length},'
            if max_length is not None:
                length_pattern += f'{max_length}}}'
            else:
                length_pattern += '}'
            pattern = f'[{combined_chars}]{length_pattern}'
        else:
            pattern = f'[{combined_chars}]*'

    if start_with:
        pattern = re.escape(start_with) + pattern
    
    if end_with:
        pattern += re.escape(end_with)
    
    return pattern

# Example usage:
# pattern = build_regex(digit=True, allowed_chars=['0', '1'], exact_one='1')
# print("Generated Regex Pattern:", pattern)


# p = build_regex(letter=False, char_spec={'1':(1,False,False)}, allowed_chars=['0','1'], max_length=8)
# print(p)
