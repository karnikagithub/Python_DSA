def maxVowels(strng,k):

    vowels = {'a','e','i','o','u'}

    left, count, result = 0,0,0

    for right in range(len(strng)):

        count += 1 if strng[right] in vowels else 0

        print(count,'countttttttttt')
        
        if right - left + 1 > k:
            count -= 1 if strng[left] in vowels else 0
            left += 1

        result = max(result,count)

    return result







def maxVowels(strng,k):

    vowels = {'a','e','i','o','u'}

    left, count, result = 0,0,0

    for right in range(len(strng)):
        
        count += 1 if strng[right] in vowels else 0

        if right - left + 1 > k:
            count -= 1 if strng[left] in vowels else 0
            left += 1
        
        result = max(result,count)

    return result





strng = 'aeiou'
k = 2

print(maxVowels(strng,k))





def maxV(s,k):
    vowels = {'a','e','i','o','u'}

    left, count, res = 0,0,0

    for right in range(len(s)):
        
        count += 1 if s[right] in vowels else 0

        if right - left + 1 > k:
            count -= 1 if s[left] in vowels else 0
            left += 1

    res = max(res,count)

    return res


strng = 'aeiou'
k = 2

print(maxV(strng,k))
