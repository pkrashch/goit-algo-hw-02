from collections import deque
import re

def is_palindrome_deque(input_string):
    """
    Checks if a given string is a palindrome using a deque.
    """
    
    # 1. Preprocessing: Make the string ready for comparison
    # Remove all non-alphanumeric characters
    cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', input_string)
    
    # Convert to lowercase to ensure case-insensitivity
    cleaned_string = cleaned_string.lower()
    
    # Check for empty string case after cleaning
    if not cleaned_string:
        return True # An empty string or a string of only spaces/punctuation is considered a palindrome, however my philological education denies it

    # 2. Add characters to the deque
    
    # Create a deque and populate it with the characters of the cleaned string
    char_deque = deque(cleaned_string)
    
    print(f"Cleaned string: '{cleaned_string}'")
    print(f"Initial deque: {char_deque}")

    # 3. Comparison from both ends
    
    while len(char_deque) > 1:
        
        # Remove and get the character from the front (left)
        first_char = char_deque.popleft()
        
        # Remove and get the character from the back (right)
        last_char = char_deque.pop()
        
        print(f"Comparing: '{first_char}' and '{last_char}'.")

        # If characters do not match, it's not a palindrome
        if first_char != last_char:
            return False

    # If the loop finishes without returning False, the string is a palindrome
    return True