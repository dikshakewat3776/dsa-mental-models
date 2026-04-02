

# 1. Two Sum
# Problem : Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# Example:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Problem Type: Array
# Pattern Identification: Looping array, checking each element, finding complementary element, return indices.
# Brute Force: Loop through the array and check if the sum of the two numbers is equal to the target.
# Optimal Thinking: Since we know the target, we can use a hash map to store the numbers and their indices.
# Optimal Solution: Use a hash map to store the numbers and their indices.
# Code:
def twoSum(nums, target):
    seen = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in seen:
            return [seen[diff], i]
        seen[nums[i]] = i
    return []
print("Two Sum:")
print(twoSum([2,7,11,15], 9))
print(twoSum([-3,2,4,3,6,8], 6))
# Edge Cases: Negative numbers, duplicates
# Variations: three sum, four sum, etc.
# Real World Applications:

# ------------------------------------------------------------

# 2. Valid anagram
# Problem : Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Example:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Explanation: Because s and t are anagrams, we return true.
# Problem Type: String
# Pattern Identification: Looping string, checking each character, finding complementary character, return boolean.
# Brute Force: Loop through the string and check if the characters are the same.
# Optimal Thinking: Since we know the strings are anagrams, we can use a hash map to store the characters and their frequencies.
# Optimal Solution: Use a hash map to store the characters and their frequencies.
# Code:
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    freq_s = {}
    freq_t = {}
    for char in s:
        freq_s[char] = freq_s.get(char, 0) + 1
    for char in t:
        freq_t[char] = freq_t.get(char, 0) + 1
    return freq_s == freq_t
print("Valid Anagram:")
print(isAnagram("anagram", "nagaram"))
print(isAnagram("cat", "car"))

# Edge Cases: Empty strings, special characters, different lengths
# Variations: Group anagrams, find all anagrams in a string, etc.
# Real World Applications: Text processing, data analysis, etc.


# ------------------------------------------------------------
# 3. Contains duplicate
# Problem : Given an integer array nums, return true if any value appears at least twice in the array, and false otherwise.
# Example:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation: Because 1 appears twice, we return true.
# Problem Type: Array
# Pattern Identification: Looping array, checking each element, finding duplicate element, return boolean.
# Brute Force: Loop through the array and check if the element is in the array.
# Optimal Thinking: Since we know the array is sorted, we can use a hash map to store the elements and their frequencies.
# Optimal Solution: Use a hash map to store the elements and their frequencies.
# Code:
def containsDuplicate(nums):
    seen = {}
    for num in nums:
        if num in seen:
            return True
        seen[num] = True
    return False
print("Contains Duplicate:")
print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))

# Edge Cases: Empty array, negative numbers, duplicates
# Variations: Find all duplicates in an array, etc.
# Real World Applications: Data analysis, data processing, etc.

# ------------------------------------------------------------
# 4. Running Sum of 1D Array
# Problem : Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Example:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Because the running sum is [1, 1+2, 1+2+3, 1+2+3+4], we return [1,3,6,10].
# Problem Type: Array
# Pattern Identification: Looping array, checking each element, finding running sum, return array.
# Brute Force: Loop through the array and check if the element is in the array.
# Optimal Thinking: Since we know the array is sorted, we can use a hash map to store the elements and their frequencies.
# Optimal Solution: Use a hash map to store the elements and their frequencies.
# Code:
def runningSum(nums):
    running_sum = 0
    for num in nums:
        running_sum += num
    return running_sum
print("Running Sum of 1D Array:")
print(runningSum([1,2,3,4]))
print(runningSum([1,1,1,1,1]))

# Edge Cases: Empty array, negative numbers, duplicates
# Variations: Find all duplicates in an array, etc.
# Real World Applications: Data analysis, data processing, etc.

# ------------------------------------------------------------
# 5. Rank transform of an array
# Problem : Given an integer array nums, return the rank transform of the array.
# Example:
# Input: nums = [40,10,20,30]
# Output: [4,1,2,3]
# Explanation: Because the rank of 40 is 4, the rank of 10 is 1, the rank of 20 is 2, and the rank of 30 is 3, we return [4,1,2,3].
# Problem Type: Array
# Pattern Identification: Looping array, checking each element, finding rank, return array.
# Brute Force: Loop through the array and check if the element is in the array.
# Optimal Thinking: Since we know the array is sorted, we can use a hash map to store the elements and their frequencies.
# Optimal Solution: Use a hash map to store the elements and their frequencies.
# Code: 
def rankTransform(nums):
    sorted_nums = sorted(nums)
    rank = {}
    for num in sorted_nums:
        if num not in rank:
            rank[num] = len(rank) + 1
    return [rank[num] for num in nums]

print("Rank Transform of an Array:")
print(rankTransform([40,10,20,30]))
print(rankTransform([1,2,3,4]))

# Edge Cases: Empty array, negative numbers, duplicates, duplicates with different ranks
# Variations: Find all duplicates in an array, etc.
# Real World Applications: Data analysis, data processing, etc.
