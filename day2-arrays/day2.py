# 1. Product of Array Except Self
# Problem : Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# Example:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Explanation: The product of all the elements except nums[0] is 24, the product of all the elements except nums[1] is 12, the product of all the elements except nums[2] is 8, and the product of all the elements except nums[3] is 6.
# Problem Type: Array
# Pattern Identification: Product of prefix and suffix
# Brute Force: Loop through the array and multiply all the elements except the current element with complexity of O(n^2)
# Optimal Thinking: Since we know the product of all the elements except the current element, we can use a prefix and suffix array to store the product of all the elements except the current element.
# Optimal Solution: Prefix product multiplied with Suffix product
# Template: Create a new array, add prefix product and suffix product to the new array
# Product Pattern : [bcd, acd, abd, abc]
# Prefix Pattern : [1, a, ab, abc] -> multiply all elements from left to right
# Suffix Pattern : [abc, bc, c, 1] -> multiply all elements from right to left
# Pattern Template:
# res = [1] * n
# prefix
# for i in range(1, n):
#     res[i] = res[i-1] * nums[i-1]
#  suffix
# right = 1
# for i in range(n-1, -1, -1):
#     res[i] *= right
#     right *= nums[i]
# Code:
def productExceptSelf(nums):
    res = [1] * len(nums)  # new array with all elements as 1
    for i in range(1, len(nums)): # prefix product
        res[i] = res[i-1] * nums[i-1]
    right = 1
    for i in range(len(nums)-1, -1, -1): # suffix product
        res[i] *= right
        right *= nums[i]
    return res
print("Product of Array Except Self:")
print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))
# Example: [1,2,3, 4]
# Prefix: [1, 1, 2, 6]
# Suffix: [24, 12, 4, 1]
# res = [1,1,1,1] -> [1,1,1,1] -> [1,1,2,1] -> [1,1,2,6]
# res[i] *= right -> res[3] *= 1 -> res[2] *= 2 -> res[1] *= 6 -> res[0] *= 6
# res = [24, 12, 8, 6]
# res = [1,1,1,1,1] -> [1,1,1,1,1] -> [1,1,1,1,1] -> [1,1,1,1,1] -> [1,1,1,1,1]
# Result: [24, 12, 8, 6]
# Edge Cases: Negative numbers, duplicates, only two numbers
# Variations: Product of Array Except Self with division, Product of Array Except Self with zero, Product of Array Except Self with negative numbers
# Real World Applications example 1: Financial risk modeling (portfolio impact excluding one asset).


# 2. Maximum Subarray
# Problem : Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# Example:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The contiguous subarray [4,-1,2,1] has the largest sum = 6.
# Problem Type: Array
# Pattern Identification: Maximum Subarray
# Brute Force: Loop through the array and find the maximum sum of all the subarrays with complexity of O(n^3) because we have to check all the subarrays.
# Optimal Thinking: We are visiting each element in the array if any prefix of element is negative it is minimising my sum so we just ignore those and move ahead with adding the current element to the sum.
# Optimal Solution: Kadane's Algorithm
# Template: Initialize first element -> Decide : continue with current sum or start a new sum -> Update overall maximum sum
# Pattern Template:
# curr = nums[0]
# max_sum = nums[0]
# for num in nums[1:]:
#     curr = max(num, curr + num)
#     max_sum = max(max_sum, curr)
# return maxSum
# Code:
def maxSubArray(nums):
    maxSum = nums[0]  # Initialize the maximum sum with the first element
    curSum = 0
    for n in nums: 
        if curSum < 0: # Remove negative prefix
            curSum = 0
        curSum += n # Add the current element to the current sum
        maxSum = max(maxSum, curSum) # Update the maximum sum if the current sum is greater than the maximum sum
    return maxSum
print("Maximum Subarray:")
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([1,2,3,4,5]))
print(maxSubArray([-1,-2,-3,-4,-5]))
# Example: [-2,1,-3,4,-1,2,1,-5,4]
# maxSum = -2 -> 1 -> 1 -> 4 -> 4 -> 5 -> 6 -> 6 -> 6
# curSum = 0 -> 1 -> 0 -> 4 -> 3 -> 5 -> 6 -> 1 -> 5
# return 6
# Edge Cases: Negative numbers, duplicates, only two numbers
# Variations: Maximum Subarray with division, Maximum Subarray with zero, Maximum Subarray with negative numbers
# Real World Applications example 1: Stock Trading / Profit Window → Find best time window to maximize profit.


# 3. Maximum Product Subarray
# Problem : Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product and return its product.
# Example:
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: The contiguous subarray [2,3] has the largest product = 6.
# Problem Type: Array
# Pattern Identification: Maximum Product Subarray
# Brute Force: Loop through the array and find the maximum product of all the subarrays with complexity of O(n^3) because we have to check all the subarrays.
# Optimal Thinking: We are visiting each element in the array and identifying the current min and max product and updating the overall maximum product.
# Optimal Solution: Kadane's Algorithm (Variant) + Dynamic Programming
# Template: Initialize maximum element as result -> Initialize current min and max to 1 -> Update current max and min product -> Update result with maximum product
# Pattern Template:
# curr_max = curr_min = res = nums[0]
# for num in nums[1:]:
#     if num < 0:
#         curr_max, curr_min = curr_min, curr_max

#     curr_max = max(num, curr_max * num)
#     curr_min = min(num, curr_min * num)
#     res = max(res, curr_max)
# Code:
def maxProductSubarray(nums):
    res = max(nums) # Initialize the result with the maximum element
    curr_min = curr_max = 1 # Initialize current min and max to 1
    for n in nums:
        curr_max = max(n, curr_max * n, curr_min * n) # Update the current max product as max of current element, current max product * current element, current min product * current element
        curr_min = min(n, curr_max * n, curr_min * n) # Update the current min product as min of current element, current max product * current element, current min product * current element
        res = max(res, curr_max) # Update the result with the maximum product
    return res
print("Maximum Product Subarray:")
print(maxProductSubarray([2,3,-2,4]))
print(maxProductSubarray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxProductSubarray([1,2,3,4,5]))
print(maxProductSubarray([-1,-2,-3,-4,-5]))
# Example: [2,3,-2,4]
# 
# curr_max = 2 -> 6 -> -2 -> -8
# curr_min = 2 -> 3 -> -6 -> -24
# res = 2 -> 6 -> 6 -> 6
# return 6
# Edge Cases: Negative numbers, duplicates, only two numbers
# Variations: Maximum Product Subarray with division, Maximum Product Subarray with zero, Maximum Product Subarray with negative numbers
# Real World Applications example 1: Volatility Analysis (Finance) → Profit/loss with gains & losses (negatives flip outcome). Also in signal processing where inversion (negative signals) can amplify output.

# 4. Majority Element
# Problem : Given an integer array nums, return the majority element. The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
# Example:
# Input: nums = [3,2,3]
# Output: 3
# Explanation: The element 3 appears more than ⌊3 / 2⌋ times.
# Problem Type: Array
# Pattern Identification: Majority Element
# Brute Force: Loop through the array and count the frequency of each element with complexity of O(n^2) or maintain a hashmap and count the frequency of each element.
# Optimal Thinking: We are visiting each element in the array and counting the frequency of each element and returning the element with frequency greater than n/2.
# Optimal Solution: Boyer-Moore Voting Algorithm
# Template: Initialize a candidate and a count -> Visit each element and update the candidate and count -> Return the candidate
# Pattern Template:
# count = 0
# candidate = None
# for num in nums:
#     if count == 0:
#         candidate = num
#     count += (1 if num == candidate else -1)
# Code:
def majorityElement(nums):
    res , count = 0, 0 # Initialize the candidate and count to 0
    for n in nums:
        if count == 0:
            res = n # Update the candidate to the current element
            count = 1 # Initialize the count to 1
        else:
            count += (1 if n == res else -1) # Update the count if the current element is the same as the candidate else decrement the count
    return res
print("Majority Element:")
print(majorityElement([3,2,3]))
print(majorityElement([1,2,3,4,5]))
print(majorityElement([-1,-2,-3,-4,-5]))
# Edge Cases: Negative numbers, duplicates, only two numbers
# Variations: Majority Element with division, Majority Element with zero, Majority Element with negative numbers
# Real World Applications example 1: Election (Find winning candidate) → Majority vote determines outcome.