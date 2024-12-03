# input:
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 9, 8] 
# join the a[0]b[-1] and so on...
# output: [18, 29, 36, 45, 54]
result = [int(str(ai) + str(bi)) for ai, bi in zip(a, reversed(b))]
print(result)



l1 = [1,5,6]
l2 = [5,6,8]

add_num = [a + b for a,b in zip(l1,l2)]
print(add_num)

# Sample dictionary
student_data = {
    'John': [25, 85, ...],    # Age, Marks, ...
    'Alice': [22, 90, ...],
    'Bob': [28, 78, ...],
    # Add more entries as needed
}

# Sort the dictionary based on age (assuming age is the first element in the values list)
sorted_student_data = dict(sorted(student_data.items(), key=lambda item: item[1][0]))

# Display the sorted dictionary
for name, values in sorted_student_data.items():
    print(f"{name}: Age {values[0]}, Marks {values[1]}, ...")



#### sum of running array

def running_sum(num):
    s = 0
    
    running_s = []
    
    for n in num:
        s += n
        running_s.append(s)
        
    return running_s
    
# print(running_sum([1,3,4,5,6]))



lst = ['JY8687', 'CH8718', 'SA8727', 'BA8729', 'MR8779', 'JI8780', 'KR8820', 
       'SH8821', 'VI8823', 'RI8824', 'RI8825', 'PO8826', 'RA8827', 'SH8828', 'DE8829', 'SK8830', 
       'DR8831', 'DR8832', 'NA8833', 'DE8836', 'SM8837', 'AB8838', 'PR8843', 'SA8844', 'AS8845', 
       'JI8847', 'PR8850', 'SH8851', 'KU8852', 'PU8854', 'DE8855']

# Initialize sets to store unique characters
numbers_set = set()
alphabets_set = set()

# Iterate through each element in the list
for item in lst:
    # Iterate through each character in the item
    for char in item:
        # Check if the character is a digit (number)
        if char.isdigit():
            numbers_set.add(char)
        # Check if the character is an alphabet
        elif char.isalpha():
            alphabets_set.add(char)

# Count the unique characters
number_count = len(numbers_set)
alphabet_count = len(alphabets_set)

# print("Count of unique numbers:", number_count)
# print("Count of unique alphabets:", alphabet_count)



def find_missing_number(arr):
    n = len(arr) + 1  # Length of the array plus one (including the missing number)
    expected_sum = (n * (n + 1)) // 2  # Expected sum of the first n natural numbers
    print(expected_sum)
    actual_sum = sum(arr)  # Actual sum of the elements in the array
    print(actual_sum)
    missing_number = expected_sum - actual_sum
    return missing_number

# Example usage
arr = [1, 2, 4, 6, 3, 7, 8]
missing_number = find_missing_number(arr)
print("The missing number is:", missing_number)



def rotate_array_slicing(arr, k):
    n = len(arr)
    k = k % n  # To handle cases where k is greater than the length of the array
    print(arr[-k:])
    print(arr[:-k])
    return arr[-k:] + arr[:-k]

# Example usage
arr = [1, 2, 3, 4, 5]
k = 3
rotated_arr = rotate_array_slicing(arr, k)
print("Rotated array:", rotated_arr)


a=[11,34,56,89,0,11,23]
# #print values '[0,89,56]' in that order using a single statement
print(a[-3:-6:-1])


a=['1',23, [1,2],45,67]
# #using a for loop print only [1,2] without using index

for i in a:
    if isinstance(i,list):
        print(i)

a = '45$55&.ab@c'
# remove special characters and print alphanumeric string of 4555abc

s=''
for i in a:
    if i.isalpha() or i.isnumeric():
        s += i
        print(i,end='')


# sort this dictionary first by key and then by value
a = {'Hyderabad': 1000, 'Mumbai': 2000, 'Chennai': 1500}

sorted_a = sorted(a.items(), key=lambda x: (x[0], x[1]))

sorted_dict = dict(sorted_a)

print(sorted_dict)




inp = [1,2,3,4,5,6,7,8]
summ = 9
out =[]
# out = [[1,8],[2,7],[3,6],[4,5]]
for i in range(len(inp)):
    for j in range(0,i+1):
        if inp[i] + inp[j] == summ:
            out.append([inp[i],inp[j]])

print(out)

seen = set()
for num in inp:
    complement = summ - num
    if complement in seen:
        out.append([num, complement])
    seen.add(num)

print(out)

def find_pairs(inp, user_inp):
    pairs = []
    left = 0
    right = len(inp) - 1
    
    while left < right:
        current_sum = inp[left] + inp[right]
        if current_sum == user_inp:
            pairs.append([inp[left], inp[right]])
            left += 1
            right -= 1
        elif current_sum < user_inp:
            left += 1
        else:
            right -= 1
    
    return pairs

# Test the function
# inp = [1, 2, 3, 4, 5, 6, 7, 8]
# user_inp = 9
# out = find_pairs(inp, user_inp)
# print(out)  # Output: [[1, 8], [2, 7], [3, 6], [4, 5]]
# In this code:

# We define a function find_pairs that takes the input list inp and the user_inp.
# We initialize two pointers, left and right, pointing to the start and end of the list respectively.
# We iterate through the list using the two pointers and check if the sum of the current pair of numbers equals user_inp.
# If the sum equals user_inp, we append the pair to the pairs list and move the pointers accordingly.
# If the sum is less than user_inp, we increment the left pointer.
# If the sum is greater than user_inp, we decrement the right pointer.
# Finally, we return the list of pairs found.



def flatten_list(lst):
    result = []
    for item in lst:
        if isinstance(item, (list, tuple)):
            result.extend(flatten_list(item))
        elif isinstance(item, dict):
            result.extend(flatten_list(item.values()))
        elif item is not None:
            result.append(item)
    return result

# Test the function with dynamic input
inp = [1, 2, [3, 4], None, {'a': 5, 'b': [6, 7]}, (8, 9)]
out = flatten_list(inp)
print(out)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Another test with dynamic input
inp2 = [1, None, [2, 3], {'x': 4, 'y': [5, None]}, (6, 7), 8]
out2 = flatten_list(inp2)
print(out2)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]


# For each item in the list, it checks its type.
# If the item is a list or tuple, it recursively calls flatten_list() on that item.
# If the item is a dictionary, it extracts the values and recursively calls flatten_list() on those values.
# If the item is not None, it appends it to the result list.
# Finally, it returns the flattened list.