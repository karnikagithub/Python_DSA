#### write a program to check given string is PALINDROME

def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_s = ''.join(char for char in s if char.isalnum()).lower()

    # Compare the string with its reverse
    return cleaned_s == cleaned_s[::-1]

# Test the function
test_string = "A man, a plan, a canal, Panama"
if is_palindrome(test_string):
    print(f"'{test_string}' is a palindrome.")
else:
    print(f"'{test_string}' is not a palindrome.")


def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_s = ''.join(char for char in s if char.isalnum()).lower()

    # Compare characters from the beginning and end of the string
    start, end = 0, len(cleaned_s) - 1

    while start < end:
        if cleaned_s[start] != cleaned_s[end]:
            return False
        start += 1
        end -= 1

    return True

# Test the function
test_string = "A man, a plan, a canal, Panama"
if is_palindrome(test_string):
    print(f"'{test_string}' is a palindrome.")
else:
    print(f"'{test_string}' is not a palindrome.")



def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_s = ''.join(char for char in s if char.isalnum()).lower()

    # Manually construct the reverse of the string
    reversed_s = ''
    for char in cleaned_s:
        reversed_s = char + reversed_s

    # Compare the original string with its reverse
    return cleaned_s == reversed_s

# Test the function
test_string = "A man, a plan, a canal, Panama"
if is_palindrome(test_string):
    print(f"'{test_string}' is a palindrome.")
else:
    print(f"'{test_string}' is not a palindrome.")