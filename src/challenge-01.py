# -*- coding: utf-8 -*-
"""
  PyGenZee Challenges, Challenge 01: Palindrome String Check
"""


import re


def is_palindrome(input_str:str, ) -> bool:
    # Remove spaces, punctuations and convert to lowercase
    normalized_str = re.sub(r'[^a-zA-Z0-9]', '', input_str).lower()


    # Check if the normalized string is equal to its reverse
    result = normalized_str == normalized_str [::-1]

    # Return the check result
    return result
    

# Test Cases
print(is_palindrome("A man, a plan, a canal, Panama!"))
print(is_palindrome("hello"))
