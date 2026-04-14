# Day 3 - Hashing

---

## 1) Top K Frequent Elements

- **LeetCode:** [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
- **Problem:** Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.
- **Pattern:** Bucket Sort (Reverse) + Frequency Map
- **Brute Force:** Sort by frequency or use heap (`O(n log n)`)
- **Optimal Idea:** Count frequencies with a hash map, then place numbers into frequency buckets and traverse from high to low
- **Template:**
  - Build `count` map: `num -> frequency`.
  - Build `freq` bucket array of size `n + 1`.
  - Put each number in `freq[frequency]`.
  - Traverse buckets in reverse until collecting `k` numbers.
- **Time / Space:** `O(n)` / `O(n)`
- **Pattern (Highlight):** Frequency map + reverse bucket traversal.
- **Pattern Template (Highlight):**
```text
count = {}
for n in nums:
    count[n] = count.get(n, 0) + 1
bucket = [[] for _ in range(len(nums) + 1)]
for n, freq in count.items():
    bucket[freq].append(n)
res = []
for i in range(len(bucket) - 1, -1, -1):
    for n in bucket[i]:
        res.append(n)
        if len(res) == k:
            return res
```

**Example**
- Input: `nums = [1,1,1,2,2,3]`, `k = 2`
- Output: `[1,2]`

**Edge Cases**
- Single element array.
- All elements have same frequency.
- All elements are distinct (`k` may still be small).

**Variations**
- Include negative numbers.
- Streaming top-k frequent updates.
- Top-k frequent words instead of integers.

**Real-World Applications**
- Trending hashtags/topics.
- Most frequent error codes in logs.

---

## 2) Longest Consecutive Sequence

- **LeetCode:** [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)
- **Problem:** Given an unsorted integer array `nums`, return the length of the longest consecutive elements sequence.
- **Pattern:** Hash Set
- **Brute Force:** Sort and scan (`O(n log n)`)
- **Optimal Idea:** Use a set and only start counting when current number is the start of a sequence (`n - 1` not present)
- **Template:**
  - Convert array to set.
  - For each number, if `n - 1` not in set, expand forward.
  - Track max sequence length.
- **Time / Space:** `O(n)` / `O(n)`
- **Pattern (Highlight):** Sequence-start detection with hash set.
- **Pattern Template (Highlight):**
```text
num_set = set(nums)
longest = 0
for n in num_set:
    if n - 1 not in num_set:
        length = 1
        while n + length in num_set:
            length += 1
        longest = max(longest, length)
return longest
```

**Example**
- Input: `nums = [100,4,200,1,3,2]`
- Output: `4` (`[1,2,3,4]`)

**Edge Cases**
- Empty array.
- Duplicates in input.
- Already fully consecutive array.

**Variations**
- Return the actual sequence, not just length.
- Longest consecutive sequence with bounds/constraints.
- Negative numbers mixed with positives.

**Real-World Applications**
- Longest consecutive active days in activity tracking.
- Continuous streak analysis in time-series events.

---

## 3) Subarray Sum Equals K

- **LeetCode:** [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)
- **Problem:** Return the number of contiguous subarrays whose sum equals `k`.
- **Pattern:** Prefix Sum + Hash Map
- **Brute Force:** Check all subarrays (`O(n^2)`)
- **Optimal Idea:** Track how many times each prefix sum appears; if `prefix - k` exists, it contributes to valid subarrays
- **Template:**
  - Initialize `prefix = 0`, `res = 0`, `prefix_map = {0:1}`.
  - For each number, update prefix.
  - Add `prefix_map[prefix - k]` to result when present.
  - Increment count of current prefix in map.
- **Time / Space:** `O(n)` / `O(n)`
- **Pattern (Highlight):** Prefix sum frequency counting.
- **Pattern Template (Highlight):**
```text
res = 0
prefix = 0
prefix_map = {0: 1}
for n in nums:
    prefix += n
    if prefix - k in prefix_map:
        res += prefix_map[prefix - k]
    prefix_map[prefix] = prefix_map.get(prefix, 0) + 1
return res
```

**Example**
- Input: `nums = [1,1,1]`, `k = 2`
- Output: `2`

**Edge Cases**
- Empty array.
- Negative numbers (sliding window does not work generally).
- `k = 0` with many zeroes.

**Variations**
- Return subarray indices/count list.
- Longest subarray with sum `k`.
- Subarray sum in 2D matrix (prefix-sum extension).

**Real-World Applications**
- Event count windows hitting thresholds.
- Financial transaction streak sums.

---

## 4) Check if Array Pairs Are Divisible by k

- **LeetCode:** [1497. Check If Array Pairs Are Divisible by k](https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/)
- **Problem:** Return `true` if array can be partitioned into pairs where each pair sum is divisible by `k`.
- **Pattern:** Modulo + Hash Map
- **Brute Force:** Try all pairings (`O(n^2)` or worse)
- **Optimal Idea:** Count remainders and ensure complementary remainder frequencies match
- **Template:**
  - Build remainder frequency map: `r = num % k`.
  - For `r = 0`, count must be even.
  - For other remainders, `count[r]` must equal `count[k-r]`.
- **Time / Space:** `O(n)` / `O(k)` (or `O(n)` map-based)
- **Pattern (Highlight):** Remainder complement matching.
- **Pattern Template (Highlight):**
```text
count = {}
for num in nums:
    r = num % k
    count[r] = count.get(r, 0) + 1
for r in count:
    if r == 0 and count[r] % 2 != 0:
        return False
    if r != 0 and count[r] != count.get(k - r, 0):
        return False
return True
```

**Example**
- Input: `nums = [1,2,3,4]`, `k = 2`
- Output: `True`

**Edge Cases**
- Odd number of elements (cannot fully pair).
- Many values with remainder `0`.
- Mixed positive and negative values.

**Variations**
- Return actual pairs, not just boolean.
- Pairing constraints (minimum/maximum pair value).
- Streaming pair-validity checks.

**Real-World Applications**
- Payment batching in divisible settlement cycles.
- Inventory pairing by normalized bucket classes.

---

## Quick Revision Checklist

- `Top K Frequent` -> count map + reverse bucket traversal
- `Longest Consecutive` -> start only where `n-1` is absent
- `Subarray Sum = K` -> prefix sum frequency map
- `Pairs Divisible by K` -> remainder complement matching
