import string_utils

s = input("Enter a string: ")

print("Number of vowels =", string_utils.count_vowels(s))
print("Reverse =", string_utils.reverse_string(s))
print("Palindrome =", string_utils.is_palindrome(s))
print("Number of words =", string_utils.count_words(s))
print("Without spaces =", string_utils.remove_spaces(s))