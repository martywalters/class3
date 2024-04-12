# string_format_checker.py

import re

def is_valid_format(input_string):
    """
    Checks if the input string adheres to the specified format.
    Returns True if valid, False otherwise.
    """
    pattern = re.compile(r'^bbbb[0-9a-f]{28}$')
    return bool(pattern.match(input_string))

# Example usage:
if __name__ == "__main__":
    test_string = "bbbb00000000000000170d0000306fb6"
    if is_valid_format(test_string):
        print(f"{test_string} is in the correct format.")
    else:
        print(f"{test_string} does not match the expected format.")
