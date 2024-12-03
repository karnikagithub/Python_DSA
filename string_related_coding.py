def find_first_index_of_most_repeated_char(input_string):
    if not input_string:
        return None  # Handle empty string case

    # Count occurrences of each character
    char_count = {}
    for i, char in enumerate(input_string):
        if char in char_count:
            char_count[char].append(i)
        else:
            char_count[char] = [i]

    # Find the character with the maximum count
    most_repeated_char = max(char_count, key=lambda k: len(char_count[k]))

    # Return the first index of the most repeated character
    return char_count[most_repeated_char][0]

# Example usage:
user_input = "hello world"
result = find_first_index_of_most_repeated_char(user_input)
print(f"The first index of the most repeated character is: {result}")




### find the length of longest_sub string with out repeatative characters from the given string

def length_of_longest_substring(s: str) -> int:
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length

# Example usage
input_string = "abcabcbb"
print(length_of_longest_substring(input_string))  # Output: 3


##### check whether the number is prime or not

num = 9

if all(num % i != 0 for i in range(2,num)):
    print('true')
else:
    print('false')



# Input string
input_string = "Sabyasachi, Techno Exponent Techno I sabyasachi"

# Convert the input string to lowercase for case-insensitive comparison
input_string = input_string.lower()
print(input_string)

# Split the string into words
words = input_string.split()
print(words)
# Initialize an empty dictionary to store word counts
word_counts = {}

# Iterate through the words and count occurrences
for word in words:
    # Remove punctuation from the word
    word = word.strip('.,')
    print(word)
    
    # Increment the count for each word in the dictionary
    word_counts[word] = word_counts.get(word, 0) + 1

# Print the output
for word, count in word_counts.items():
    print(f"{word.capitalize()} - {count}")




def first_non_repeating_char(string):
    char_count = {}  # Dictionary to store the frequency of each character
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in string:
        if char_count[char] == 1:
            return char
    return None  # If no non-repeating character found

# Example usage
string = "leetcode"
result = first_non_repeating_char(string)
if result:
    print("The first non-repeating character is:", result)
else:
    print("No non-repeating character found in the string.")



def is_valid_parentheses(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

# Test cases
string1 = "()[]"
string2 = "([)]}{"
string3 = "{[]}"

print(is_valid_parentheses(string1))  # Output: True
print(is_valid_parentheses(string2))  # Output: False
print(is_valid_parentheses(string3))  # Output: True



ip= "VIRAT KHOLI"
op= "TARIV ILOHK"


ip_split = ip.split(' ')
print(ip_split)
op_str = []

for word in ip_split:
    op_str.append(word[::-1])
    o=' '.join(op_str)

text = "python world"
reversed_text = ''.join(reversed(text))
print(reversed_text)
    
print(o)


