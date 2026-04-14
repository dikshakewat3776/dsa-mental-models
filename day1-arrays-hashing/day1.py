

# 1. Two Sum
# Problem : Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# Example:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Problem Type: Array
# Pattern Identification: Looping array, looking up an array, repeated lookup
# Brute Force: Loop through the array and check if the sum of the two numbers is equal to the target with complexity of O(n^2)
# Optimal Thinking: Since we know the target, we can use a hash map to store the numbers and their indices.
# Optimal Solution: Use a hash map for faster lookups of both keys and indices with complexity of O(n)
# Template: Create hashmap -> loop items -> check if diff is in hashmap -> return indices
# Pattern: Hashing (HashMap)
# Pattern Template:
# seen = {}
# for i in range(len(nums)):
#     diff = target - nums[i]
#     if diff in seen:
#         return [seen[diff], i]
#     seen[nums[i]] = i
# return []
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
# Example:
# Input: nums = [2,7,11,15], target = 9
# seen = {2: 0, 7: 1, 11: 2, 15: 3}
# diff = 9 - 2 = 7
# diff in seen: True
# return [seen[diff], i] = [1, 0]
# return [0, 1]
# Edge Cases: Negative numbers, duplicates, only two numbers
# Variations: three sum, four sum, k sum, etc.
# Real World Applications example 1: Fraud - transaction 1 + transaction 2 = target or suspicious transaction
# Real World Applications example 2: recommendation system - item 1 + item 2 = target or similar item


# ------------------------------------------------------------
# 2. Contains duplicate
# Problem : Given an integer array nums, return true if any value appears at least twice in the array, and false otherwise.
# Example:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation: Because 1 appears twice, we return true.
# Problem Type: Array
# Pattern Identification: Looping array, checking each element, uniqueness check.
# Brute Force: Loop through the array and check if the element is in the array with complexity of O(n^2)
# Optimal Thinking: Since we know the array is sorted, we can use a hash map to store the elements and their frequencies with complexity of O(n)
# Optimal Solution: Use a hash map to store the elements and their frequencies with complexity of O(n)
# Template: Create hashset -> loop items -> check if item is in hashset -> return True
# Pattern: Hashing (HashSet)
# Pattern Template:
# seen = {}
# for num in nums:
#     if num in seen:
#         return True
#     seen[num] = True
# return False
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
# Example:
# Input: nums = [1,2,3,4]
# seen = {1: True, 2: True, 3: True, 4: True}
# num = 1
# num in seen: True
# return True
# Edge Cases: Empty array, negative numbers, duplicates
# Variations: Find all duplicates in an array, count duplicates, etc.
# Real World Applications example 1: Data validation - check if a user has already registered
# Real World Applications example 2: Data validation - check if a user has already logged in

# ------------------------------------------------------------

# 3. Valid anagram
# Problem : Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Example:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Explanation: Because s and t are anagrams, we return true.
# Problem Type: String
# Pattern Identification: Looping string, existence check, string character lookup, frequency check.
# Brute Force: Loop through the string and check if the characters are the same.
# Optimal Thinking: Since we know the strings are anagrams, we can use a hash map to store the characters and their frequencies.
# Optimal Solution: Use a hash map to store the characters and their frequencies.
# Template: Create hashmap -> loop items -> increment count -> check if frequencies are the same -> return True
# Pattern: Hashing (HashMap)
# Pattern Template:
# freq_s = {}
# freq_t = {}
# for c in s:
#     freq_s[c] = freq_s.get(c, 0) + 1
# for c in t:
#     freq_t[c] = freq_t.get(c, 0) + 1
# return freq_s == freq_t
# Code:
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    freq_s = {}
    freq_t = {}
    for c in s:
        freq_s[c] = freq_s.get(c, 0) + 1
    for c in t:
        freq_t[c] = freq_t.get(c, 0) + 1
    return freq_s == freq_t   
# Example:
# Input: s = "anagram", t = "nagaram"
# freq_s = {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
# freq_t = {'n': 1, 'a': 3, 'g': 1, 'r': 1, 'm': 1}
# freq_s == freq_t: True
# return True
# Edge Cases: Empty strings, special characters, different lengths
# Variations: Group anagrams, find all anagrams in a string, etc.
# Real World Applications example 1: NLP - word 1 + word 2 = target or similar word, duplicate word check
# Real World Applications example 2: Permutation - word 1 + word 2 = target or similar word, duplicate word check

# ------------------------------------------------------------

# 4. Running Sum of 1D Array
# Problem : Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Example:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Because the running sum is [1, 1+2, 1+2+3, 1+2+3+4], we return [1,3,6,10].
# Problem Type: Array
# Pattern Identification: Looping array, checking each element, prefix sum, return array.
# Brute Force: Loop through the array and create a new array with the running sum.
# Optimal Thinking: Since we are adding elements we can do this in place by adding previous element to current element
# Template: Loop through the array -> add previous element to current element in place -> return array
# Pattern: Array (Prefix Sum)
# Pattern Template:
# for i in range(1, len(nums)):
#     nums[i] += nums[i - 1]
# return nums
# Code:
def runningSum(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums
print("Running Sum of 1D Array:")
print(runningSum([1,2,3,4]))
print(runningSum([1,1,1,1,1]))
# Example:
# Input: nums = [1, 3, 6, 10]
# nums[1] = nums[1] + nums[0] = 3 + 1 = 4
# nums[2] = nums[2] + nums[1] = 6 + 4 = 10
# nums[3] = nums[3] + nums[2] = 10 + 10 = 20
# return [1,4,10,20]
# Edge Cases: Empty array, negative numbers, duplicates
# Variations: Find all duplicates in an array, etc.
# Real World Applications example 1: Data analysis - calculate the running sum of a stock price
# Real World Applications example 2: Data analysis - Cummulative profit/loss/revenue calculation


# ------------------------------------------------------------
# 5. Rank transform of an array
# Problem : Given an integer array nums, return the rank transform of the array.
# Example:
# Input: nums = [40,10,20,30]
# Output: [4,1,2,3]
# Explanation: Because the rank of 40 is 4, the rank of 10 is 1, the rank of 20 is 2, and the rank of 30 is 3, we return [4,1,2,3].
# Problem Type: Array
# Pattern Identification: Looping array, checking each element, uniqueness check, return array.
# Brute Force: Loop through the array and check if the element is in the array.
# Optimal Thinking: Since we know the array is sorted, we can use a hash map to store the elements and their frequencies.
# Optimal Solution: Use a hash map to store the elements and their frequencies.
# Template: Sort the array -> rank the elements starting from 1 -> map the elements to the rank -> return the rank of the elements
# Pattern: Hashing (HashMap)
# Pattern Template:
# s = sorted(nums)
# rank = {num: i + 1 for i, num in enumerate(s)}
# return [rank[num] for num in nums]
# Code: 
def rankTransform(nums):
    s = sorted(nums)
    rank = {num: i + 1 for i, num in enumerate(s)}
    return [rank[num] for num in nums]
print("Rank Transform of an Array:")
print(rankTransform([40,10,20,30]))
print(rankTransform([1,2,3,4]))
# Example:
# Input : nums = [40,10,20,30]
# s = [10,20,30,40]
# rank = {10: 1, 20: 2, 30: 3, 40: 4}
# nums = [40,10,20,30]
# Edge Cases: Empty array, negative numbers, duplicates, duplicates with different ranks
# Variations: Relative rank, absolute rank, coordinate compression, etc.
# Real World Applications example 1: Data normalization - large values to compressed ranks
# Real World Applications example 2: Data embedding - rank similarity score in vector space