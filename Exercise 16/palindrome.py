def is_palindrome(word):
    # Base case: If the word is empty or has only one character, it's a palindrome
    if len(word) <= 1:
        return True
    # Recursive case: Check if the first and last characters are equal
    elif word[0] == word[-1]:
        # Recursively check the rest of the word (excluding the first and last characters)
        return is_palindrome(word[1:-1])
    else:
        # If the first and last characters are not equal, it's not a palindrome
        return False

# Test the function with the words "anna" and "tacocat"
word1 = "anna"
word2 = "tacocat"

print(f'Is "{word1}" a palindrome? {is_palindrome(word1)}')
print(f'Is "{word2}" a palindrome? {is_palindrome(word2)}')
