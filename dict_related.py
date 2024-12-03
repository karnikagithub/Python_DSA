# print("Hello")
# Python Assignment Questions
#1. Join items of a given list using "-" and print the string. 
days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sun', 'mon', 'mon']

joined_days = '-'.join(days)
print(joined_days)




#2. count the occurrences of a particular element in the list and output #highest occurring element
#days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sun', 'mon', 'mon']
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


# 3. Merge dictionaries a and b. The resultant dict must contain all items of 
# both dicts. If key is common then the value of key in resultant dict 
# must be the sum of value in a and b.
a = {'x': 1, 'y': 2, 'z': 3}
b = {'a': 4, 'b': 5, 'y': 6}
def merge(a,b):
  
  merged_dict = {}

  # Merge dictionary a into merged_dict
  for key, value in a.items():
      merged_dict[key] = value

  # Merge dictionary b into merged_dict
  for key, value in b.items():
      if key in merged_dict:
          # If key exists in both dictionaries, sum their values
          merged_dict[key] += value
      else:
          # If key doesn't exist in merged_dict, add it
          merged_dict[key] = value

  return merged_dict


print(merge(a,b))
  
#   #4. Return the Item with highest value count
items = [{'Delhi': 3}, {'Mumbai': 9}, {'Goa': 7}, {'Gujrat': 4}] 
def highest_count(items):
  
  # Initialize variables to keep track of the maximum value and the corresponding item
  max_value = float('-inf')  # Initialize with negative infinity to handle cases where all counts are negative
  max_item = None

  # Iterate through the list of dictionaries
  for item in items:
      for city, count in item.items():
          if count > max_value:
              max_value = count
              max_item = {city: count}
  
  return max_item

print(highest_count(items))


 #5. Implement a group_by_owners function that:
#Accepts a dictionary containing the file owner name for each file name.
#Returns a dictionary containing a list of file names for each owner #name, in any order.
file = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} 
#the group_by_owners function should return 
# output = {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.
def group_by_owners(files):
  grouped_files = {}

  # Iterate through the files dictionary
  for file, owner in files.items():
      # Check if the owner already exists in the grouped_files dictionary
      if owner in grouped_files:
          # If the owner exists, append the file to the list of files for that owner
          grouped_files[owner].append(file)
      else:
          # If the owner doesn't exist, create a new list with the file and add it to the dictionary
          grouped_files[owner] = [file]

  return grouped_files
 

print(group_by_owners(file))




def reverse_vowels(s):
    vowels = 'aeiouAEIOU'
    # Extract vowels from the string
    vowel_list = [char for char in s if char in vowels]

    # Reverse the list of vowels
    reversed_vowels = vowel_list[::-1]

    # Replace the vowels in the original string with reversed vowels
    result = ''
    vowel_index = 0
    for char in s:
        if char in vowels:
            result += reversed_vowels[vowel_index]
            vowel_index += 1
        else:
            result += char

    return result

# Example usage:
s = "hello"
print(reverse_vowels(s))  # Output: "hollo werld"



def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort intervals based on start times
    intervals.sort(key=lambda x: x[0])

    merged_intervals = [intervals[0]]  # Initialize with the first interval

    # Iterate through the sorted intervals
    for interval in intervals[1:]:
        # Check for overlap with the last merged interval
        if interval[0] <= merged_intervals[-1][1]:
            # Merge overlapping intervals by taking the maximum end time
            merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
        else:
            # Add non-overlapping intervals to the result
            merged_intervals.append(interval)

    return merged_intervals

# Example usage:
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge_intervals(intervals))  # Output: [[1,6],[8,10],[15,18]]




addresses={ 
    "addresses": [ 
        { 
            "address1": "1745 T Street Southeast", 
            "address2": "", 
            "city": "Washington", 
            "state": "DC", 
            "postalCode": "20020", 
            "coordinates": { 
                "lat": 38.867033, 
                "lng": -76.979235 
            } 
        }, 
        { 
            "address1": "6007 Applegate Lane", 
            "address2": "", 
            "city": "Louisville", 
            "state": "KY", 
            "postalCode": "40219", 
            "coordinates": { 
                "lat": 38.1343013, 
                "lng": -85.6498512 
            } 
        } 
] 
} 
# 1745 T Street Southeast,,Washington,DC,20020 
# 6007 Applegate Lane,,Louisville,KY,40219

for address in addresses["addresses"]:
    print(f"{address['address1']}, {address['city']}, {address['state']}, {address['postalCode']}")