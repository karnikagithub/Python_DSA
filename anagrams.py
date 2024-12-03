#### to check whether given strings are ANAGRAM or NOT

s = 'ate'
b = 'eat'


def isAnagram(s,b):
    f = {}
    
    for char in s:
        if char in f:
            f[char] += 1
        else:
            f[char] = 1

    for char in b:
        if char not in f: return False
        elif f[char] == 1: del f[char]
        else: f[char] -= 1

    return not f

print(isAnagram(s,b))


def is_anagram(str1, str2):
    # Remove spaces and lower the cases for case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sorted characters of both strings are equal
    return sorted(str1) == sorted(str2)


ana_list = ["eat", "tea", "tan", "ate", "nat", "bat"]

dct = {}

for index,i in enumerate(ana_list):
    s = sorted(i)
    dct[index] = s
    
# print(dct)

lst = {}

for k, v in dct.items():
   
    if str(v) in lst.keys():
        temp = lst[str(v)] 
        temp.append(k)
        lst[str(v)] = temp
    else:
        lst[str(v)] = [k]

fl = []
for i in lst.values():
    il = sorted([ana_list[j] for j in i])
    fl.append(il)
print(fl)
    

input_li = ["eat", "tea", "tan", "ate", "nat", "bat"]

dic  = {}
for ind,val in enumerate(input_li):
    s = ''.join(sorted(val))
    # Another method using setdefault function of dictionary
    dic.setdefault(s,[]).append(input_li[ind])
    
print([sorted(i) for i in dic.values()])


from collections import defaultdict

def group_anagrams(input_li):
    anagrams = defaultdict(list)
    
    for word in input_li:
        # Sort the word and use the sorted version as the key
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    
    # Return the grouped anagrams as a list
    return list(anagrams.values())