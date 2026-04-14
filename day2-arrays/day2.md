# Day 2 - Arrays

---

## 1) Product of Array Except Self

- **LeetCode:** [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)
- **Problem:** Given an integer array `nums`, return an array `answer` where `answer[i]` is the product of all elements of `nums` except `nums[i]`.
- **Pattern:** Prefix product + suffix product
- **Brute Force:** For each index, multiply all other elements (`O(n^2)`)
- **Optimal Idea:** Build prefix products in result array, then multiply by running suffix product
- **Template:**
  - Initialize result array with `1`s.
  - Fill prefix products left to right.
  - Track running suffix product right to left.
  - Multiply suffix into result at each index.
- **Time / Space:** `O(n)` / `O(1)` extra (excluding output array)
- **Pattern (Highlight):** Prefix and suffix product multiplication.
- **Pattern Template (Highlight):**
```text
res = [1] * len(nums)
for i in range(1, len(nums)):
    res[i] = res[i - 1] * nums[i - 1]
right = 1
for i in range(len(nums) - 1, -1, -1):
    res[i] *= right
    right *= nums[i]
return res
```

**Example**
- Input: `nums = [1,2,3,4]`
- Output: `[24,12,8,6]`

**Edge Cases**
- Contains one or more zeros.
- Negative numbers.
- Length is 2.
- Large products may overflow in fixed-width integer languages.

**Variations**
- Version using division (when no zero).
- Return in-place vs separate output array.
- Modular arithmetic product variants.
- Product except self in 2D flattening scenarios.

**Real-World Applications**
- Portfolio analysis: estimate impact excluding one asset at a time.
- Reliability modeling: product of component factors excluding one component.

---

## 2) Maximum Subarray

- **LeetCode:** [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
- **Problem:** Find the contiguous subarray with the largest sum and return that sum.
- **Pattern:** Kadane's Algorithm
- **Brute Force:** Check all subarrays (`O(n^3)` or `O(n^2)` with prefix sums)
- **Optimal Idea:** If current running sum becomes negative, reset it; keep track of best sum seen
- **Template:**
  - Initialize `maxSum` and running `curSum`.
  - Traverse elements once.
  - Reset `curSum` if it becomes negative.
  - Update `maxSum` each step.
- **Time / Space:** `O(n)` / `O(1)`
- **Pattern (Highlight):** Kadane's running-sum reset.
- **Pattern Template (Highlight):**
```text
maxSum = nums[0]
curSum = 0
for n in nums:
    if curSum < 0:
        curSum = 0
    curSum += n
    maxSum = max(maxSum, curSum)
return maxSum
```

**Example**
- Input: `nums = [-2,1,-3,4,-1,2,1,-5,4]`
- Output: `6`

**Edge Cases**
- All numbers negative.
- Single element array.
- All positive numbers.
- Mix with zeros.

**Variations**
- Return subarray indices as well as sum.
- Circular maximum subarray.
- Maximum average subarray.
- Exactly `k` length maximum-sum subarray.

**Real-World Applications**
- Trading analytics: best profit window in a time series.
- Signal analysis: strongest contiguous segment in noisy measurements.

---

## 3) Maximum Product Subarray

- **LeetCode:** [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)
- **Problem:** Find the contiguous subarray with the largest product and return that product.
- **Pattern:** Dynamic tracking of current max/min products
- **Brute Force:** Check products of all subarrays (`O(n^3)` or `O(n^2)`)
- **Optimal Idea:** A negative can flip min <-> max, so track both at each step
- **Template:**
  - Keep `curr_max`, `curr_min`, and global `res`.
  - For each element, compute products with previous max/min (use temp values).
  - Update current max/min using element and two products.
  - Update global result.
- **Time / Space:** `O(n)` / `O(1)`
- **Pattern (Highlight):** Track both min and max product each step.
- **Pattern Template (Highlight):**
```text
res = max(nums)
curr_min = 1
curr_max = 1
for n in nums:
    temp_max = curr_max * n
    temp_min = curr_min * n
    curr_max = max(n, temp_max, temp_min)
    curr_min = min(n, temp_max, temp_min)
    res = max(res, curr_max)
return res
```

**Example**
- Input: `nums = [2,3,-2,4]`
- Output: `6`

**Edge Cases**
- Contains zeros that reset product chain.
- All negative numbers.
- Single element array.
- Signs flipping across adjacent negatives.
- Large magnitudes and overflow concerns.

**Variations**
- Return subarray boundaries, not only product.
- Circular maximum product variants.
- Minimum product subarray.
- Log-transform based analysis variants.

**Real-World Applications**
- Volatility modeling: compounded gains/losses where negatives flip outcomes.
- Sensor/signal systems: identify contiguous interval with strongest multiplicative effect.

---

## 4) Majority Element

- **LeetCode:** [169. Majority Element](https://leetcode.com/problems/majority-element/)
- **Problem:** Return the element that appears more than `floor(n/2)` times.
- **Pattern:** Boyer-Moore Voting Algorithm
- **Brute Force:** Count frequency for each element (`O(n^2)`) or use hash map (`O(n)`, extra space)
- **Optimal Idea:** Pair-cancel different elements; remaining candidate is majority
- **Template:**
  - Initialize `candidate` and `count`.
  - If `count == 0`, set current element as candidate.
  - Increment for same candidate, decrement otherwise.
  - Return final candidate.
- **Time / Space:** `O(n)` / `O(1)`
- **Pattern (Highlight):** Boyer-Moore vote cancellation.
- **Pattern Template (Highlight):**
```text
candidate, count = 0, 0
for n in nums:
    if count == 0:
        candidate = n
    count += 1 if n == candidate else -1
return candidate
```

**Example**
- Input: `nums = [3,2,3]`
- Output: `3`

**Edge Cases**
- Single element.
- Negative values.
- Candidate changes multiple times.
- No guaranteed majority (requires verification pass).

**Variations**
- Majority element II (`> n/3`).
- Find all elements above frequency threshold.
- Streaming majority tracking.
- Weighted majority vote.

**Real-World Applications**
- Elections/polls: determine candidate with strict majority support.
- Consensus systems: identify dominant label/opinion in repeated votes.

---

## Quick Revision Checklist

- `Product Except Self` -> prefix * suffix trick
- `Maximum Subarray` -> Kadane (reset on negative running sum)
- `Maximum Product Subarray` -> track both `curr_max` and `curr_min`
- `Majority Element` -> Boyer-Moore vote cancellation

