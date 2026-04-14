# Day 1 - Arrays & Hashing

---

## 1) Two Sum

- **LeetCode:** [1. Two Sum](https://leetcode.com/problems/two-sum/)
- **Problem:** Given an array `nums` and an integer `target`, return indices of two numbers such that they add up to `target`.
- **Pattern:** Hash map for complement lookup
- **Brute Force:** Check all pairs (`O(n^2)`)
- **Optimal Idea:** Store seen numbers and their indices; for each number, check if `target - num` is already seen
- **Template:**
  - Create hash map `seen`.
  - Loop through numbers with index.
  - Compute complement `target - num`.
  - If complement is in `seen`, return indices.
  - Otherwise store current number and index.
- **Time / Space:** `O(n)` / `O(n)`
- **Pattern (Highlight):** Complement lookup using a hash map.
- **Pattern Template (Highlight):**
```text
seen = {}
for i in range(len(nums)):
    diff = target - nums[i]
    if diff in seen:
        return [seen[diff], i]
    seen[nums[i]] = i
```

**Example**
- Input: `nums = [2,7,11,15], target = 9`
- Output: `[0,1]`

**Edge Cases**
- Array length is 2.
- Negative numbers and zero.
- Duplicate values in array.
- No valid pair exists (if allowed by variant).

**Variations**
- Return values instead of indices.
- Return all valid pairs.
- Sorted array version (two pointers).
- 3Sum / 4Sum / k-Sum.

**Real-World Applications**
- Fraud checks: detect two transactions that combine to a suspicious total.
- Recommendation bundling: find two items whose scores/prices match a target.

---

## 2) Contains Duplicate

- **LeetCode:** [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
- **Problem:** Return `true` if any value appears at least twice; otherwise return `false`.
- **Pattern:** Hash set / hash map for membership check
- **Brute Force:** Compare every pair (`O(n^2)`)
- **Optimal Idea:** Track seen elements while iterating
- **Template:**
  - Initialize empty `seen` set/map.
  - Traverse each element once.
  - If already in `seen`, return `True`.
  - Else insert element into `seen`.
  - Return `False` after full traversal.
- **Time / Space:** `O(n)` / `O(n)`
- **Pattern (Highlight):** Membership check with hash set.
- **Pattern Template (Highlight):**
```text
seen = set()
for num in nums:
    if num in seen:
        return True
    seen.add(num)
return False
```

**Example**
- Input: `nums = [1,2,3,1]`
- Output: `True`

**Edge Cases**
- Empty array.
- Single element array.
- Negative values.
- Very large input size.

**Variations**
- Return duplicate elements instead of boolean.
- Count frequencies of all elements.
- Find first duplicate by index order.
- Detect duplicates within distance `k`.

**Real-World Applications**
- Data validation: detect duplicate user IDs, emails, or records.
- Event processing: identify repeated events in logs/streams.

---

## 3) Valid Anagram

- **LeetCode:** [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)
- **Problem:** Given strings `s` and `t`, return `true` if `t` is an anagram of `s`.
- **Pattern:** Frequency counting with hash maps
- **Brute Force:** Sort and compare (or repeated matching)
- **Optimal Idea:** Count each character frequency and compare maps
- **Template:**
  - If lengths differ, return `False`.
  - Count character frequencies for `s`.
  - Count character frequencies for `t`.
  - Compare the two maps.
- **Time / Space:** `O(n)` / `O(1)` for fixed alphabet, otherwise `O(n)`
- **Pattern (Highlight):** Character frequency counting.
- **Pattern Template (Highlight):**
```text
if len(s) != len(t):
    return False
freq_s, freq_t = {}, {}
for c in s:
    freq_s[c] = freq_s.get(c, 0) + 1
for c in t:
    freq_t[c] = freq_t.get(c, 0) + 1
return freq_s == freq_t
```

**Example**
- Input: `s = "anagram", t = "nagaram"`
- Output: `True`

**Edge Cases**
- Empty strings.
- Different lengths.
- Repeated characters.
- Case sensitivity or punctuation constraints.

**Variations**
- Unicode anagram checks.
- Ignore spaces/punctuation and case.
- Group anagrams from a list.
- Find all anagram indices in a string.

**Real-World Applications**
- NLP preprocessing: detect reordered-word equivalence for text normalization.
- Search/query systems: match queries independent of character order in puzzles/games.

---

## 4) Running Sum of 1D Array

- **LeetCode:** [1480. Running Sum of 1D Array](https://leetcode.com/problems/running-sum-of-1d-array/)
- **Problem:** Return running sum where `runningSum[i] = nums[0] + ... + nums[i]`.
- **Pattern:** Prefix sum
- **Brute Force:** For each index, sum from start each time (`O(n^2)`)
- **Optimal Idea:** Build running total in one pass (in-place possible)
- **Template:**
  - Start loop from index `1`.
  - Add previous cumulative sum to current element.
  - Continue to end and return array.
- **Time / Space:** `O(n)` / `O(1)` extra (in-place)
- **Pattern (Highlight):** Prefix sum accumulation.
- **Pattern Template (Highlight):**
```text
for i in range(1, len(nums)):
    nums[i] += nums[i - 1]
return nums
```

**Example**
- Input: `nums = [1,2,3,4]`
- Output: `[1,3,6,10]`

**Edge Cases**
- Empty array.
- Single element.
- Negative numbers.
- Overflow concerns in fixed-width integer languages.

**Variations**
- Build new output array (non-mutating).
- Prefix-sum array for range queries.
- 2D prefix sums for matrices.
- Streaming cumulative totals.

**Real-World Applications**
- Finance dashboards: cumulative revenue/profit over time.
- Analytics pipelines: rolling totals for usage, clicks, or sales.

---

## 5) Rank Transform of an Array

- **LeetCode:** [1331. Rank Transform of an Array](https://leetcode.com/problems/rank-transform-of-an-array/)
- **Problem:** Replace each value with its rank (smallest unique value gets rank 1).
- **Pattern:** Sorting + hash map
- **Brute Force:** Compare each element with all others (`O(n^2)`)
- **Optimal Idea:** Sort unique values, assign increasing ranks, map back
- **Template:**
  - Extract and sort unique values.
  - Assign rank starting from `1`.
  - Map original elements to ranks.
  - Return mapped rank array.
- **Time / Space:** `O(n log n)` / `O(n)`
- **Pattern (Highlight):** Sorting + rank mapping.
- **Pattern Template (Highlight):**
```text
unique_sorted = sorted(set(nums))
rank = {num: i + 1 for i, num in enumerate(unique_sorted)}
return [rank[num] for num in nums]
```

**Example**
- Input: `nums = [40,10,20,30]`
- Output: `[4,1,2,3]`

**Edge Cases**
- Empty array.
- Duplicate values share same rank.
- Negative values.
- Already sorted or reverse-sorted arrays.

**Variations**
- Dense vs sparse ranking styles.
- Relative rank labels (medals/titles).
- Coordinate compression for larger problems.
- Cross-dataset ranking.

**Real-World Applications**
- Data normalization: compress large values into rank-based features.
- Leaderboards/scoring: map raw scores to positions for comparison.

---

## Quick Revision Checklist

- `Two Sum` -> complement + hash map
- `Contains Duplicate` -> membership check with set/map
- `Valid Anagram` -> compare frequency maps
- `Running Sum` -> prefix sum in one pass
- `Rank Transform` -> sort unique + rank mapping

