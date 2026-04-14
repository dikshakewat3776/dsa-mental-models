# 1. Top K Frequent Elements
# Problem: Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
# Follow up: The algorithm's time complexity must be better than O(n log n), where n is the array's size.
# Pattern: Frequency
# Brute: Sort by frequency with O(n log n) time complexity and the max heap to get the top k elements with O(k log n) time complexity as long as k < n.
# Optimize: We can still do this in O(n) time complexity by using a hash map to count frequencies but it will still be O(n log n)
# Optimal Thinking: We can use a bucket sort to count frequencies, where keys are counts and values are lists of numbers that have that count with O(n) time complexity
# Optimal Solution: Bucket Sort is being used since each number can have a frequency of up to n. Say the size of array is n, then the frequency of each number can be at most n.
# Optimal Solution: We will reverse bucket sort such that i is the index of the frequency and the value is the list of numbers that have that frequency achieving linear time complexity.
# Template: Create frequency list -> Count frequencies -> fill bucket with max count at the end -> reverse traversal of bucket to get the top k elements
# Pattern: Bucket Sort (Reverse)
# Pattern Template:
# count = {}
# for num in nums:
#     count[num] = count.get(num, 0) + 1
# bucket = [[] for _ in range(len(nums)+1)]
# for num, freq in count.items():
#     bucket[freq].append(num)
# res = []
# for i in range(len(bucket)-1, -1, -1):
#     for num in bucket[i]:
#         res.append(num)
#         if len(res) == k:
#             return res
# Code:
def topKFrequent(nums, k):
    count = {}
    # Create a frequency list of size n + 1
    freq = [[] for _ in range(len(nums) + 1)]
    # Count the frequency of each number
    for n in nums:
        count[n] = count.get(n, 0) + 1
    # Fill the frequency list
    for n, count in count.items():
        freq[count].append(n)
    # Reverse traversal of frequency list to get the top k elements
    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) >= k:
                return res
    return res
print("Top K Frequent Elements:")
print(topKFrequent([1,1,1,2,2,3], 2))
# Example:
# Array: [1,1,1,2,2,3]
# freq list: [[], [], [], [], [], []]
# count: {1: 3, 2: 2, 3: 1} -> sorted by frequency
# freq[3].append(1) -> max count is put at the end of the list -> freq[3] = [1]
# freq[2].append(2) -> second max count is put at the end of the list -> freq[2] = [2]
# freq[1].append(3) -> min count is put at the end of the list -> freq[1] = [3]
# freq list: [[], [3], [2], [1]]
# res: [1, 2] -> reverse traversal of freq list to get the top k elements
# Edge Cases: one element in the array, all elements have the same frequency, all elements have different frequencies
# Variations: Top K Frequent Elements with negative numbers, Top K Frequent Elements with duplicates
# Real World Applications example 1: Trending hashtags (top K), Most frequent errors in logs (top K)

# 2. Longest Consecutive Sequence
# Problem: Given an unsorted array of integers nums, return the length of the longest consecutive sequence.
# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Follow up: The algorithm's time complexity must be better than O(n log n), where n is the array's size.
# Pattern: Consecutive Sequence
# Brute: Sort the array and then traverse the array to find the longest consecutive sequence with O(n log n) time complexity
# Optimize: We track sequences by ensuring we visit each number only once with O(n) time complexity
# Optimal Thinking: We go through each element and check if it is the start of a sequence by checking if the previous number is not in the set. 
# If it is the start of a sequence, we then check how long the sequence is by checking if the next number is in the set and adding to the longest sequence length.
# Template: Traverse the array -> check if the current number is the start of a sequence -> check if the next number is in the set -> add to the longest sequence length
# Pattern: Hashing (Set)
# Pattern Template:
# num_set = set(nums)
# longest = 0
# for num in num_set:
#     if num - 1 not in num_set:  # start
#         length = 1
#         while num + length in num_set:
#             length += 1 
#         longest = max(longest, length)
# Code:
def longestConsecutive(nums):
    # Create a set
    unique = set(nums)
    print(unique)
    longest = 0
    for n in unique: # iterate over set and not nums
        # Check if the current number is the start of a sequence by checking left neighbor is not in the set
        if (n-1) not in unique:
            length = 0
            # Check how long the sequence is
            while (n+length) in unique:
                length += 1
            longest = max(longest, length)
    return longest
print("Longest Consecutive Sequence:")
print(longestConsecutive([100,4,200,1,3,2]))
# Example:
# Array: [100,4,200,1,3,2]
# unique: {1, 2, 3, 100, 4, 200}
# | n   | (n-1) in set? | Start Sequence? | length after while | longest |
# | --- | ------------- | --------------- | ------------------ | ------- |
# | 100 | 99 ❌          | ✅ Yes           | 1                  | 1       |
# | 4   | 3 ✅           | ❌ No            | —                  | 1       |
# | 200 | 199 ❌         | ✅ Yes           | 1                  | 1       |
# | 1   | 0 ❌           | ✅ Yes           | 4                  | 4       |
# | 3   | 2 ✅           | ❌ No            | —                  | 4       |
# | 2   | 1 ✅           | ❌ No            | —                  | 4       |
# Edge Cases: empty array, array with one element, array with all elements the same, array with all elements in consecutive order
# Variations: Longest Consecutive Sequence with negative numbers, Longest Consecutive Sequence with duplicates
# Real World Applications example 1: Longest consecutive days of stock price increase, Longest consecutive days of temperature increase


# 3. Subarray Sum Equals K
# Problem: Given an integer array nums and an integer k, return the number of contiguous subarrays whose sum equals to k.
# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2
# Follow up: The algorithm's time complexity must be better than O(n^2), where n is the array's size.
# Pattern: Subarray Sum Equals K
# Brute: Traverse the array and check all subarrays with O(n^2) time complexity
# Optimize: We can use a hash map to store the sum of subarrays with O(n) time complexity.
# Optimal Thinking: We can use a hash map to store prefix sums with their corresponding counts with O(n) time complexity.
# Template: Traverse the array -> store prefix sums in hash map -> check if the current sum - k is in the hash map -> add the count of the current sum - k to the result
# Pattern: Hashing (Prefix Sum)
# Pattern Template:
# count = 0
# prefix = 0
# map = {0:1}
# for num in nums:
#     prefix += num
#     if prefix - k in map:
#         count += map[prefix - k]
#     map[prefix] = map.get(prefix, 0) + 1
# Code:
def subarraySum(nums, k):
    res = 0
    prefix = 0
    prefix_map = {0:1}
    for n in nums:
        prefix += n
        if prefix - k in prefix_map:
            res += prefix_map[prefix - k]
        prefix_map[prefix] = prefix_map.get(prefix, 0) + 1
    return res
print("Subarray Sum Equals K:")
print(subarraySum([1,1,1], 2))
# Example:
# Array: [1,1,1] and k = 2
# prefix: 0
# prefix_map: {0:1}
# | n | prefix | prefix - k | res | prefix_map           |
# | - | ------ | ---------- | --- | -------------------- |
# | 1 | 1      | -1         | 0   | {0:1, 1:1}           |
# | 1 | 2      | 0          | 1   | {0:1, 1:1, 2:1}      |
# | 1 | 3      | 1          | 2   | {0:1, 1:1, 2:1, 3:1} |
# Edge Cases: empty array, array with one element, array with all elements the same, array with all elements in consecutive order
# Variations: Subarray Sum Equals K with negative numbers, Subarray Sum Equals K with duplicates
# Real World Applications example : Monitoring → time window sum = threshold, Analytics → event aggregation

# 4. Check if Array pairs are divisible by k
# Problem: Given an array of integers nums and an integer k, return true if nums can be partitioned into pairs such that the sum of each pair is divisible by k, otherwise return false.
# Example 1:
# Input: nums = [1,2,3,4], k = 2
# Output: true
# Example 2:
# Input: nums = [1,2,3,4], k = 3
# Output: false
# Follow up: The algorithm's time complexity must be better than O(n^2), where n is the array's size.
# Pattern: Array Pairs Divisible by K
# Brute: Traverse and pair all elements with O(n^2) time complexity 
# Optimize: We can use a hash map to store the remainder of each number with O(n) time complexity.
# Optimal Thinking: We can use a hash map to store the remainder of each number with O(n) time complexity.
# Template : r pairs with (k - r) exists in the hash map
# Pattern: Modulo + HashMap
# Pattern Template:
# count = {}
# for num in nums:
#     r = num % k
#     count[r] = count.get(r, 0) + 1
# for r in count:
#     if r == 0:
#         if count[r] % 2 != 0:
#             return False
#     elif count[r] != count.get(k - r, 0):
#         return False
# return True
def canPair(nums, k):
    count = {}
    for num in nums:
        r = num % k
        count[r] = count.get(r, 0) + 1
    for r in count:
        if r == 0:
            if count[r] % 2 != 0:
                return False
        elif count[r] != count.get(k - r, 0):
            return False
    return True
print("Check if Array pairs are divisible by k:")
print(canPair([1,2,3,4], 2))
# Example:
# Array: [1,2,3,4] and k = 2
# count: {1: 1, 0: 2}
# | r | count[r] | count.get(k - r, 0) |
# | - | -------- | ------------------- |
# | 1 | 1        | 1                   |
# | 0 | 2        | 2                   |
# Edge Cases: empty array, array with one element, array with all elements the same, array with all elements in consecutive order
# Variations: Check if Array pairs are divisible by k with negative numbers, Check if Array pairs are divisible by k with duplicates
# Real World Applications example : Inventory management → pair items by weight, Payment batching (divisible settlements)