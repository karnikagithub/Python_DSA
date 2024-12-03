from collections import Counter

def sort_by_frequency(input_list):
    # Count the frequency of each element
    freq_counter = Counter(input_list)
    
    # Sort the elements by frequency and original order
    sorted_elements = sorted(input_list, key=lambda x: (-freq_counter[x], input_list.index(x)))
    
    return sorted_elements

# input_list = [1, 2, 3, 2, 4, 3, 1, 2]
input_list = [-199,6,7,-199,3,5]
output = sort_by_frequency(input_list)
print(output)



def repeatedCharacters(s):
    seen_letters = set()

    for c in s:
        if c in seen_letters:
            return c
        else:
            seen_letters.add(c)

    return None  # Return None if there are no repeated characters

# Test the function
print(repeatedCharacters("abcdefg"))  # Output: None
print(repeatedCharacters("abcdefgg"))  # Output: g

days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sun', 'mon', 'mon']


def findMaxOccuringString(days):
  highest_oocurence = {}
  
  for day in days:
    highest_oocurence.setdefault(day,[]).append(day)
    
  repeated_days = []
  for key,val in highest_oocurence.items():
    if len(val) >= 2:
      repeated_days.append(val)
      
  return repeated_days

print(findMaxOccuringString(days))