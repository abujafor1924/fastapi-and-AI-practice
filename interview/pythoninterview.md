# Complete Python DSA Interview Solutions

I'll provide solutions for all 100 problems with detailed comments. Let me break this down into multiple sections for readability.

---

## SECTION 1: ARRAYS (Problems 1-15)

### 1. Two Sum
```python
def twoSum(nums, target):
    """
    Find two numbers that add up to target.
    Time: O(n), Space: O(n)
    """
    # Dictionary to store number and its index
    num_map = {}
    
    # Iterate through array
    for i, num in enumerate(nums):
        # Calculate complement needed
        complement = target - num
        
        # If complement exists, return both indices
        if complement in num_map:
            return [num_map[complement], i]
        
        # Store current number with its index
        num_map[num] = i
    
    return []  # Should never reach here if solution exists
```

### 2. Best Time to Buy and Sell Stock
```python
def maxProfit(prices):
    """
    Find maximum profit from buying and selling once.
    Time: O(n), Space: O(1)
    """
    # Track minimum price seen so far and maximum profit
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        # Update minimum price if current is lower
        if price < min_price:
            min_price = price
        # Calculate profit if selling at current price
        else:
            profit = price - min_price
            max_profit = max(max_profit, profit)
    
    return max_profit
```

### 3. Contains Duplicate
```python
def containsDuplicate(nums):
    """
    Check if any value appears at least twice.
    Time: O(n), Space: O(n)
    """
    # Use set to track seen numbers
    seen = set()
    
    for num in nums:
        # If number already seen, return True
        if num in seen:
            return True
        seen.add(num)
    
    return False
```

### 4. Product of Array Except Self
```python
def productExceptSelf(nums):
    """
    Return array where each element is product of all elements except itself.
    Time: O(n), Space: O(n) for output (O(1) extra space)
    """
    n = len(nums)
    result = [1] * n
    
    # First pass: products of all elements to the left
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]
    
    # Second pass: multiply with products of all elements to the right
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
    
    return result
```

### 5. Maximum Subarray (Kadane's Algorithm)
```python
def maxSubArray(nums):
    """
    Find contiguous subarray with largest sum.
    Time: O(n), Space: O(1)
    """
    # Initialize with first element
    current_sum = nums[0]
    max_sum = nums[0]
    
    # Start from second element
    for num in nums[1:]:
        # Either extend existing subarray or start new one
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum
```

### 6. Maximum Product Subarray
```python
def maxProduct(nums):
    """
    Find contiguous subarray with largest product.
    Time: O(n), Space: O(1)
    """
    if not nums:
        return 0
    
    # Track max and min products (min needed for negative numbers)
    max_so_far = nums[0]
    min_so_far = nums[0]
    result = nums[0]
    
    for num in nums[1:]:
        # Store previous max before updating
        prev_max = max_so_far
        
        # Max can be: current num, current num * max, or current num * min
        max_so_far = max(num, max(num * max_so_far, num * min_so_far))
        min_so_far = min(num, min(num * prev_max, num * min_so_far))
        
        result = max(result, max_so_far)
    
    return result
```

### 7. Find Minimum in Rotated Sorted Array
```python
def findMin(nums):
    """
    Find minimum in rotated sorted array using binary search.
    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        # If mid > right, minimum is in right half
        if nums[mid] > nums[right]:
            left = mid + 1
        # Else minimum is in left half including mid
        else:
            right = mid
    
    return nums[left]
```

### 8. Search in Rotated Sorted Array
```python
def search(nums, target):
    """
    Search in rotated sorted array using binary search.
    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        # Check which half is sorted
        if nums[left] <= nums[mid]:  # Left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1
```

### 9. 3Sum
```python
def threeSum(nums):
    """
    Find all triplets that sum to zero.
    Time: O(n²), Space: O(n) for sorting
    """
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 2):
        # Skip duplicates for i
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Two pointer approach for remaining elements
        left, right = i + 1, n - 1
        target = -nums[i]
        
        while left < right:
            current_sum = nums[left] + nums[right]
            
            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    
    return result
```

### 10. Container With Most Water
```python
def maxArea(height):
    """
    Find two lines that together with x-axis form container with most water.
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(height) - 1
    max_water = 0
    
    while left < right:
        # Calculate area with current pointers
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height
        max_water = max(max_water, current_area)
        
        # Move the pointer with smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water
```

### 11. Move Zeroes
```python
def moveZeroes(nums):
    """
    Move all zeroes to end while maintaining relative order.
    Time: O(n), Space: O(1)
    """
    # Position to place next non-zero element
    non_zero_pos = 0
    
    # Move all non-zero elements to front
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_pos] = nums[i]
            non_zero_pos += 1
    
    # Fill remaining positions with zeroes
    for i in range(non_zero_pos, len(nums)):
        nums[i] = 0
```

### 12. Remove Duplicates from Sorted Array
```python
def removeDuplicates(nums):
    """
    Remove duplicates in-place from sorted array.
    Time: O(n), Space: O(1)
    """
    if not nums:
        return 0
    
    # Position for next unique element
    unique_pos = 0
    
    for i in range(1, len(nums)):
        if nums[i] != nums[unique_pos]:
            unique_pos += 1
            nums[unique_pos] = nums[i]
    
    return unique_pos + 1
```

### 13. Merge Sorted Array
```python
def merge(nums1, m, nums2, n):
    """
    Merge two sorted arrays into nums1.
    Time: O(m+n), Space: O(1)
    """
    # Start from the end of both arrays
    p1, p2 = m - 1, n - 1
    p = m + n - 1
    
    # Merge from end to beginning
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    
    # If any elements left in nums2, copy them
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1
```

### 14. Majority Element
```python
def majorityElement(nums):
    """
    Find element appearing more than n/2 times using Boyer-Moore Voting.
    Time: O(n), Space: O(1)
    """
    candidate = None
    count = 0
    
    # Find candidate
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    
    return candidate
```

### 15. Missing Number
```python
def missingNumber(nums):
    """
    Find missing number in array of 0 to n.
    Time: O(n), Space: O(1)
    """
    n = len(nums)
    # Sum of numbers 0 to n
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    
    return expected_sum - actual_sum
```

---

## SECTION 2: STRINGS (Problems 16-30)

### 16. Valid Anagram
```python
def isAnagram(s, t):
    """
    Check if t is anagram of s.
    Time: O(n), Space: O(n)
    """
    if len(s) != len(t):
        return False
    
    # Count frequency of each character
    char_count = {}
    
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in t:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] == 0:
            del char_count[char]
    
    return len(char_count) == 0
```

### 17. Group Anagrams
```python
def groupAnagrams(strs):
    """
    Group strings by anagram.
    Time: O(n * k * log k), Space: O(n)
    """
    from collections import defaultdict
    
    anagram_groups = defaultdict(list)
    
    for s in strs:
        # Sort string to get key
        sorted_s = ''.join(sorted(s))
        anagram_groups[sorted_s].append(s)
    
    return list(anagram_groups.values())
```

### 18. Longest Common Prefix
```python
def longestCommonPrefix(strs):
    """
    Find longest common prefix among strings.
    Time: O(n * min_length), Space: O(1)
    """
    if not strs:
        return ""
    
    # Start with first string as prefix
    prefix = strs[0]
    
    for s in strs[1:]:
        # Reduce prefix until it matches
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix
```

### 19. Valid Palindrome
```python
def isPalindrome(s):
    """
    Check if string is palindrome ignoring non-alphanumeric.
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric characters
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare ignoring case
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True
```

### 20. Longest Substring Without Repeating Characters
```python
def lengthOfLongestSubstring(s):
    """
    Find length of longest substring without repeating characters.
    Time: O(n), Space: O(min(m, n))
    """
    char_index = {}  # Store last position of each character
    max_length = 0
    start = 0
    
    for end, char in enumerate(s):
        # If character repeats, move start
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        
        # Update character position
        char_index[char] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length
```

### 21. Longest Palindromic Substring
```python
def longestPalindrome(s):
    """
    Find longest palindromic substring.
    Time: O(n²), Space: O(1)
    """
    if not s:
        return ""
    
    start, end = 0, 0
    
    for i in range(len(s)):
        # Check odd length palindrome
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left > end - start:
                start, end = left, right
            left -= 1
            right += 1
        
        # Check even length palindrome
        left, right = i, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left > end - start:
                start, end = left, right
            left -= 1
            right += 1
    
    return s[start:end + 1]
```

### 22. Reverse Words in a String
```python
def reverseWords(s):
    """
    Reverse words in a string.
    Time: O(n), Space: O(n)
    """
    # Split by spaces and filter empty strings
    words = s.split()
    # Reverse and join
    return ' '.join(reversed(words))
```

### 23. String Compression
```python
def compress(chars):
    """
    Compress string by counting consecutive characters.
    Time: O(n), Space: O(1)
    """
    write = 0  # Position to write
    read = 0   # Position to read
    
    while read < len(chars):
        char = chars[read]
        count = 0
        
        # Count consecutive characters
        while read < len(chars) and chars[read] == char:
            read += 1
            count += 1
        
        # Write character
        chars[write] = char
        write += 1
        
        # Write count if more than 1
        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1
    
    return write
```

### 24. Roman to Integer
```python
def romanToInt(s):
    """
    Convert Roman numeral to integer.
    Time: O(n), Space: O(1)
    """
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    # Process from right to left
    for char in reversed(s):
        current_value = roman_map[char]
        # If current is smaller than previous, subtract
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        prev_value = current_value
    
    return total
```

### 25. Integer to Roman
```python
def intToRoman(num):
    """
    Convert integer to Roman numeral.
    Time: O(1), Space: O(1)
    """
    # Define values and corresponding symbols
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    
    result = []
    
    for value, symbol in zip(values, symbols):
        while num >= value:
            result.append(symbol)
            num -= value
    
    return ''.join(result)
```

### 26. Implement strStr()
```python
def strStr(haystack, needle):
    """
    Find first occurrence of needle in haystack.
    Time: O(n*m), Space: O(1)
    """
    if not needle:
        return 0
    
    n, m = len(haystack), len(needle)
    
    for i in range(n - m + 1):
        # Check if substring matches
        if haystack[i:i+m] == needle:
            return i
    
    return -1
```

### 27. Decode String
```python
def decodeString(s):
    """
    Decode encoded string (e.g., "3[a2[c]]" -> "accaccacc").
    Time: O(n), Space: O(n)
    """
    stack = []
    current_num = 0
    current_str = ""
    
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            # Push current state to stack
            stack.append((current_str, current_num))
            current_str = ""
            current_num = 0
        elif char == ']':
            # Pop from stack and decode
            prev_str, num = stack.pop()
            current_str = prev_str + current_str * num
        else:
            current_str += char
    
    return current_str
```

### 28. Minimum Window Substring
```python
def minWindow(s, t):
    """
    Find minimum window substring containing all characters of t.
    Time: O(n), Space: O(n)
    """
    from collections import Counter
    
    if not s or not t:
        return ""
    
    # Count characters in t
    t_count = Counter(t)
    window_count = {}
    
    required = len(t_count)
    formed = 0
    left, right = 0, 0
    
    # Track minimum window
    min_length = float('inf')
    min_left = 0
    
    while right < len(s):
        # Expand window
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1
        
        if char in t_count and window_count[char] == t_count[char]:
            formed += 1
        
        # Try to shrink window
        while left <= right and formed == required:
            char = s[left]
            
            # Update minimum window
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_left = left
            
            # Remove left character
            window_count[char] -= 1
            if char in t_count and window_count[char] < t_count[char]:
                formed -= 1
            
            left += 1
        
        right += 1
    
    return "" if min_length == float('inf') else s[min_left:min_left + min_length]
```

### 29. Zigzag Conversion
```python
def convert(s, numRows):
    """
    Convert string to zigzag pattern.
    Time: O(n), Space: O(n)
    """
    if numRows == 1 or numRows >= len(s):
        return s
    
    # Create rows
    rows = [''] * numRows
    current_row = 0
    going_down = False
    
    for char in s:
        rows[current_row] += char
        
        # Change direction at top or bottom
        if current_row == 0 or current_row == numRows - 1:
            going_down = not going_down
        
        current_row += 1 if going_down else -1
    
    return ''.join(rows)
```

### 30. Count and Say
```python
def countAndSay(n):
    """
    Generate nth term of count-and-say sequence.
    Time: O(2^n), Space: O(2^n)
    """
    if n == 1:
        return "1"
    
    # Get previous term
    prev = countAndSay(n - 1)
    result = ""
    count = 1
    
    # Count consecutive digits
    for i in range(len(prev)):
        if i + 1 < len(prev) and prev[i] == prev[i + 1]:
            count += 1
        else:
            result += str(count) + prev[i]
            count = 1
    
    return result
```

---

## SECTION 3: HASH TABLE (Problems 31-38)

### 31. Two Sum (Already solved as #1)
### 32. Happy Number
```python
def isHappy(n):
    """
    Check if number is happy.
    Time: O(log n), Space: O(log n)
    """
    seen = set()
    
    while n != 1 and n not in seen:
        seen.add(n)
        # Calculate sum of squares of digits
        n = sum(int(digit) ** 2 for digit in str(n))
    
    return n == 1
```

### 33. Isomorphic Strings
```python
def isIsomorphic(s, t):
    """
    Check if two strings are isomorphic.
    Time: O(n), Space: O(n)
    """
    if len(s) != len(t):
        return False
    
    s_to_t = {}
    t_to_s = {}
    
    for char_s, char_t in zip(s, t):
        # Check mapping from s to t
        if char_s in s_to_t:
            if s_to_t[char_s] != char_t:
                return False
        else:
            s_to_t[char_s] = char_t
        
        # Check mapping from t to s
        if char_t in t_to_s:
            if t_to_s[char_t] != char_s:
                return False
        else:
            t_to_s[char_t] = char_s
    
    return True
```

### 34. Word Pattern
```python
def wordPattern(pattern, s):
    """
    Check if pattern matches string.
    Time: O(n), Space: O(n)
    """
    words = s.split()
    if len(pattern) != len(words):
        return False
    
    pattern_to_word = {}
    word_to_pattern = {}
    
    for p, word in zip(pattern, words):
        # Check pattern to word mapping
        if p in pattern_to_word:
            if pattern_to_word[p] != word:
                return False
        else:
            pattern_to_word[p] = word
        
        # Check word to pattern mapping
        if word in word_to_pattern:
            if word_to_pattern[word] != p:
                return False
        else:
            word_to_pattern[word] = p
    
    return True
```

### 35. Top K Frequent Elements
```python
def topKFrequent(nums, k):
    """
    Find k most frequent elements.
    Time: O(n log k), Space: O(n)
    """
    from collections import Counter
    import heapq
    
    # Count frequencies
    freq = Counter(nums)
    
    # Use min heap to keep k most frequent
    heap = []
    for num, count in freq.items():
        heapq.heappush(heap, (count, num))
        if len(heap) > k:
            heapq.heappop(heap)
    
    return [num for count, num in heap]
```

### 36. Intersection of Two Arrays
```python
def intersection(nums1, nums2):
    """
    Find intersection of two arrays.
    Time: O(n + m), Space: O(n)
    """
    set1 = set(nums1)
    set2 = set(nums2)
    return list(set1.intersection(set2))
```

### 37. Longest Consecutive Sequence
```python
def longestConsecutive(nums):
    """
    Find longest consecutive sequence.
    Time: O(n), Space: O(n)
    """
    if not nums:
        return 0
    
    num_set = set(nums)
    max_length = 0
    
    for num in num_set:
        # Check if it's start of sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            # Count consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            
            max_length = max(max_length, current_length)
    
    return max_length
```

### 38. Find Duplicate Number
```python
def findDuplicate(nums):
    """
    Find duplicate number in array (Floyd's algorithm).
    Time: O(n), Space: O(1)
    """
    # Use slow and fast pointers (cycle detection)
    slow = nums[0]
    fast = nums[0]
    
    # Find intersection point
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    # Find start of cycle (duplicate)
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow
```

---

## SECTION 4: STACK (Problems 39-46)

### 39. Valid Parentheses
```python
def isValid(s):
    """
    Check if parentheses are valid.
    Time: O(n), Space: O(n)
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:  # Closing bracket
            # Check if stack is empty or top doesn't match
            if not stack or stack.pop() != mapping[char]:
                return False
        else:  # Opening bracket
            stack.append(char)
    
    return len(stack) == 0
```

### 40. Min Stack
```python
class MinStack:
    """
    Stack that supports getMin in O(1).
    """
    def __init__(self):
        self.stack = []
        self.min_stack = []  # Track minimums
    
    def push(self, val):
        self.stack.append(val)
        # Update min stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self):
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()
    
    def top(self):
        return self.stack[-1] if self.stack else None
    
    def getMin(self):
        return self.min_stack[-1] if self.min_stack else None
```

### 41. Daily Temperatures
```python
def dailyTemperatures(temperatures):
    """
    Find days until warmer temperature.
    Time: O(n), Space: O(n)
    """
    result = [0] * len(temperatures)
    stack = []  # Store indices of temperatures
    
    for i, temp in enumerate(temperatures):
        # While current temp is warmer than stack top
        while stack and temp > temperatures[stack[-1]]:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index
        stack.append(i)
    
    return result
```

### 42. Next Greater Element
```python
def nextGreaterElement(nums1, nums2):
    """
    Find next greater element for each element.
    Time: O(n), Space: O(n)
    """
    next_greater = {}
    stack = []
    
    # Process nums2 to find next greater for each
    for num in nums2:
        while stack and num > stack[-1]:
            smaller = stack.pop()
            next_greater[smaller] = num
        stack.append(num)
    
    # Remaining elements have no next greater
    while stack:
        next_greater[stack.pop()] = -1
    
    return [next_greater[num] for num in nums1]
```

### 43. Evaluate Reverse Polish Notation
```python
def evalRPN(tokens):
    """
    Evaluate Reverse Polish Notation expression.
    Time: O(n), Space: O(n)
    """
    stack = []
    operators = {'+', '-', '*', '/'}
    
    for token in tokens:
        if token not in operators:
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            else:  # division
                # Python division with truncation toward zero
                stack.append(int(a / b))
    
    return stack[0]
```

### 44. Largest Rectangle in Histogram
```python
def largestRectangleArea(heights):
    """
    Find largest rectangle in histogram.
    Time: O(n), Space: O(n)
    """
    stack = []  # Store indices with increasing heights
    max_area = 0
    
    for i, h in enumerate(heights + [0]):  # Add sentinel
        # Process taller heights
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i - stack[-1] - 1 if stack else i
            max_area = max(max_area, height * width)
        stack.append(i)
    
    return max_area
```

### 45. Simplify Path
```python
def simplifyPath(path):
    """
    Simplify Unix file path.
    Time: O(n), Space: O(n)
    """
    parts = path.split('/')
    stack = []
    
    for part in parts:
        if not part or part == '.':
            continue
        elif part == '..':
            if stack:
                stack.pop()
        else:
            stack.append(part)
    
    return '/' + '/'.join(stack)
```

### 46. Decode String (Already solved as #27)

---

## SECTION 5: QUEUE (Problems 47-50)

### 47. Implement Queue Using Stacks
```python
class MyQueue:
    """
    Queue implementation using two stacks.
    """
    def __init__(self):
        self.stack1 = []  # For push
        self.stack2 = []  # For pop/peek
    
    def push(self, x):
        self.stack1.append(x)
    
    def pop(self):
        self._move()
        return self.stack2.pop()
    
    def peek(self):
        self._move()
        return self.stack2[-1]
    
    def empty(self):
        return not self.stack1 and not self.stack2
    
    def _move(self):
        """Move elements from stack1 to stack2 if stack2 is empty"""
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
```

### 48. Implement Stack Using Queues
```python
from collections import deque

class MyStack:
    """
    Stack implementation using queues.
    """
    def __init__(self):
        self.q = deque()
    
    def push(self, x):
        # Add new element to back
        self.q.append(x)
        # Rotate queue to make new element front
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
    
    def pop(self):
        return self.q.popleft()
    
    def top(self):
        return self.q[0]
    
    def empty(self):
        return not self.q
```

### 49. Sliding Window Maximum
```python
from collections import deque

def maxSlidingWindow(nums, k):
    """
    Find maximum in each sliding window.
    Time: O(n), Space: O(k)
    """
    result = []
    dq = deque()  # Store indices
    
    for i, num in enumerate(nums):
        # Remove elements outside current window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # Remove smaller elements from back
        while dq and nums[dq[-1]] < num:
            dq.pop()
        
        dq.append(i)
        
        # Add maximum to result when window is complete
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result
```

### 50. First Unique Character
```python
def firstUniqChar(s):
    """
    Find first non-repeating character.
    Time: O(n), Space: O(1) (26 characters max)
    """
    from collections import Counter
    
    # Count characters
    char_count = Counter(s)
    
    # Find first character with count 1
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i
    
    return -1
```

---

## SECTION 6: LINKED LIST (Problems 51-60)

```python
# Define ListNode for all linked list problems
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### 51. Reverse Linked List
```python
def reverseList(head):
    """
    Reverse a linked list iteratively.
    Time: O(n), Space: O(1)
    """
    prev = None
    current = head
    
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    
    return prev
```

### 52. Merge Two Sorted Lists
```python
def mergeTwoLists(l1, l2):
    """
    Merge two sorted linked lists.
    Time: O(n+m), Space: O(1)
    """
    dummy = ListNode(0)
    current = dummy
    
    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    # Attach remaining nodes
    if l1:
        current.next = l1
    if l2:
        current.next = l2
    
    return dummy.next
```

### 53. Linked List Cycle
```python
def hasCycle(head):
    """
    Detect if linked list has a cycle.
    Time: O(n), Space: O(1)
    """
    if not head:
        return False
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    
    return False
```

### 54. Detect Cycle II
```python
def detectCycle(head):
    """
    Find node where cycle begins.
    Time: O(n), Space: O(1)
    """
    if not head:
        return None
    
    # Find intersection point
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None
    
    # Find cycle start
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow
```

### 55. Middle of Linked List
```python
def middleNode(head):
    """
    Find middle node of linked list.
    Time: O(n), Space: O(1)
    """
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow
```

### 56. Remove Nth Node From End
```python
def removeNthFromEnd(head, n):
    """
    Remove nth node from end of list.
    Time: O(n), Space: O(1)
    """
    dummy = ListNode(0)
    dummy.next = head
    
    first = dummy
    second = dummy
    
    # Move first n+1 steps ahead
    for _ in range(n + 1):
        first = first.next
    
    # Move both until first reaches end
    while first:
        first = first.next
        second = second.next
    
    # Remove nth node
    second.next = second.next.next
    
    return dummy.next
```

### 57. Palindrome Linked List
```python
def isPalindrome(head):
    """
    Check if linked list is palindrome.
    Time: O(n), Space: O(1)
    """
    if not head or not head.next:
        return True
    
    # Find middle
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse second half
    prev = None
    while slow:
        next_temp = slow.next
        slow.next = prev
        prev = slow
        slow = next_temp
    
    # Compare halves
    first = head
    second = prev
    
    while second:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next
    
    return True
```

### 58. Add Two Numbers
```python
def addTwoNumbers(l1, l2):
    """
    Add two numbers represented by linked lists.
    Time: O(max(n,m)), Space: O(max(n,m))
    """
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        
        current = current.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    
    return dummy.next
```

### 59. Intersection of Two Linked Lists
```python
def getIntersectionNode(headA, headB):
    """
    Find intersection node of two linked lists.
    Time: O(n+m), Space: O(1)
    """
    if not headA or not headB:
        return None
    
    # Get lengths
    lenA = 0
    lenB = 0
    currA = headA
    currB = headB
    
    while currA:
        lenA += 1
        currA = currA.next
    
    while currB:
        lenB += 1
        currB = currB.next
    
    # Align start points
    currA = headA
    currB = headB
    
    if lenA > lenB:
        for _ in range(lenA - lenB):
            currA = currA.next
    elif lenB > lenA:
        for _ in range(lenB - lenA):
            currB = currB.next
    
    # Find intersection
    while currA and currB:
        if currA == currB:
            return currA
        currA = currA.next
        currB = currB.next
    
    return None
```

### 60. Copy List with Random Pointer
```python
class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def copyRandomList(head):
    """
    Copy linked list with random pointers.
    Time: O(n), Space: O(n)
    """
    if not head:
        return None
    
    # Create mapping from original to copy
    mapping = {}
    
    # First pass: create copies
    current = head
    while current:
        mapping[current] = Node(current.val)
        current = current.next
    
    # Second pass: set next and random pointers
    current = head
    while current:
        mapping[current].next = mapping.get(current.next)
        mapping[current].random = mapping.get(current.random)
        current = current.next
    
    return mapping[head]
```

---

## SECTION 7: BINARY TREE (Problems 61-75)

```python
# Define TreeNode for all tree problems
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### 61. Maximum Depth of Binary Tree
```python
def maxDepth(root):
    """
    Find maximum depth of binary tree.
    Time: O(n), Space: O(h) where h is height
    """
    if not root:
        return 0
    
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    
    return 1 + max(left_depth, right_depth)
```

### 62. Same Tree
```python
def isSameTree(p, q):
    """
    Check if two binary trees are identical.
    Time: O(n), Space: O(h)
    """
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
```

### 63. Invert Binary Tree
```python
def invertTree(root):
    """
    Invert binary tree (mirror).
    Time: O(n), Space: O(h)
    """
    if not root:
        return None
    
    # Swap children
    root.left, root.right = root.right, root.left
    
    # Recursively invert subtrees
    invertTree(root.left)
    invertTree(root.right)
    
    return root
```

### 64. Balanced Binary Tree
```python
def isBalanced(root):
    """
    Check if binary tree is height-balanced.
    Time: O(n), Space: O(h)
    """
    def height(node):
        if not node:
            return 0
        
        left_height = height(node.left)
        if left_height == -1:
            return -1
        
        right_height = height(node.right)
        if right_height == -1:
            return -1
        
        if abs(left_height - right_height) > 1:
            return -1
        
        return 1 + max(left_height, right_height)
    
    return height(root) != -1
```

### 65. Diameter of Binary Tree
```python
def diameterOfBinaryTree(root):
    """
    Find diameter (longest path between any two nodes).
    Time: O(n), Space: O(h)
    """
    diameter = [0]  # Use list for mutable reference
    
    def height(node):
        if not node:
            return 0
        
        left_height = height(node.left)
        right_height = height(node.right)
        
        # Update diameter
        diameter[0] = max(diameter[0], left_height + right_height)
        
        return 1 + max(left_height, right_height)
    
    height(root)
    return diameter[0]
```

### 66. Binary Tree Level Order Traversal
```python
from collections import deque

def levelOrder(root):
    """
    Level order traversal (BFS).
    Time: O(n), Space: O(n)
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result
```

### 67. Lowest Common Ancestor
```python
def lowestCommonAncestor(root, p, q):
    """
    Find lowest common ancestor of two nodes.
    Time: O(n), Space: O(h)
    """
    if not root or root == p or root == q:
        return root
    
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    
    if left and right:
        return root
    
    return left if left else right
```

### 68. Validate Binary Search Tree
```python
def isValidBST(root):
    """
    Validate if tree is a BST.
    Time: O(n), Space: O(h)
    """
    def validate(node, low, high):
        if not node:
            return True
        
        if node.val <= low or node.val >= high:
            return False
        
        return (validate(node.left, low, node.val) and
                validate(node.right, node.val, high))
    
    return validate(root, float('-inf'), float('inf'))
```

### 69. Kth Smallest Element in BST
```python
def kthSmallest(root, k):
    """
    Find kth smallest element in BST.
    Time: O(n), Space: O(h)
    """
    stack = []
    current = root
    count = 0
    
    while stack or current:
        # Go to leftmost node
        while current:
            stack.append(current)
            current = current.left
        
        # Process node
        current = stack.pop()
        count += 1
        
        if count == k:
            return current.val
        
        # Go to right subtree
        current = current.right
    
    return None
```

### 70. Path Sum
```python
def hasPathSum(root, targetSum):
    """
    Check if root-to-leaf path sum equals target.
    Time: O(n), Space: O(h)
    """
    if not root:
        return False
    
    # Check if leaf
    if not root.left and not root.right:
        return root.val == targetSum
    
    targetSum -= root.val
    return (hasPathSum(root.left, targetSum) or
            hasPathSum(root.right, targetSum))
```

### 71. Binary Tree Right Side View
```python
def rightSideView(root):
    """
    Get right side view of binary tree.
    Time: O(n), Space: O(n)
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        rightmost = None
        
        for _ in range(level_size):
            node = queue.popleft()
            rightmost = node.val
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(rightmost)
    
    return result
```

### 72. Serialize and Deserialize Binary Tree
```python
class Codec:
    """
    Serialize and deserialize binary tree.
    """
    def serialize(self, root):
        """Convert tree to string."""
        if not root:
            return "null"
        
        return (str(root.val) + "," +
                self.serialize(root.left) + "," +
                self.serialize(root.right))
    
    def deserialize(self, data):
        """Convert string to tree."""
        def dfs(values):
            val = next(values)
            if val == "null":
                return None
            
            node = TreeNode(int(val))
            node.left = dfs(values)
            node.right = dfs(values)
            return node
        
        return dfs(iter(data.split(',')))
```

### 73. Construct Binary Tree from Preorder and Inorder
```python
def buildTree(preorder, inorder):
    """
    Construct binary tree from preorder and inorder traversals.
    Time: O(n), Space: O(n)
    """
    if not preorder or not inorder:
        return None
    
    # First element of preorder is root
    root_val = preorder[0]
    root = TreeNode(root_val)
    
    # Find root index in inorder
    root_index = inorder.index(root_val)
    
    # Recursively build left and right subtrees
    root.left = buildTree(
        preorder[1:1+root_index],
        inorder[:root_index]
    )
    root.right = buildTree(
        preorder[1+root_index:],
        inorder[root_index+1:]
    )
    
    return root
```

### 74. Symmetric Tree
```python
def isSymmetric(root):
    """
    Check if tree is symmetric.
    Time: O(n), Space: O(h)
    """
    def isMirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        
        return (t1.val == t2.val and
                isMirror(t1.left, t2.right) and
                isMirror(t1.right, t2.left))
    
    return isMirror(root, root)
```

### 75. Count Good Nodes
```python
def goodNodes(root):
    """
    Count good nodes (nodes where path from root doesn't have larger value).
    Time: O(n), Space: O(h)
    """
    def dfs(node, max_val):
        if not node:
            return 0
        
        # Check if current node is good
        is_good = 1 if node.val >= max_val else 0
        
        # Update max value for children
        max_val = max(max_val, node.val)
        
        return (is_good +
                dfs(node.left, max_val) +
                dfs(node.right, max_val))
    
    return dfs(root, float('-inf'))
```

---

## SECTION 8: HEAP / PRIORITY QUEUE (Problems 76-82)

### 76. Kth Largest Element
```python
import heapq

def findKthLargest(nums, k):
    """
    Find kth largest element.
    Time: O(n log k), Space: O(k)
    """
    # Min heap of size k
    heap = []
    
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]
```

### 77. Top K Frequent Elements (Already solved as #35)

### 78. Merge K Sorted Lists
```python
def mergeKLists(lists):
    """
    Merge k sorted linked lists.
    Time: O(n log k), Space: O(k)
    """
    if not lists:
        return None
    
    # Create min heap of (value, index, node)
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
    
    dummy = ListNode(0)
    current = dummy
    
    while heap:
        val, i, node = heapq.heappop(heap)
        current.next = node
        current = current.next
        
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    
    return dummy.next
```

### 79. Find Median From Data Stream
```python
import heapq

class MedianFinder:
    """
    Find median from data stream.
    """
    def __init__(self):
        self.small = []  # Max heap (store negative)
        self.large = []  # Min heap
    
    def addNum(self, num):
        # Add to small heap
        heapq.heappush(self.small, -num)
        
        # Balance: ensure every element in small <= every element in large
        if (self.small and self.large and
            -self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # Balance sizes
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
    
    def findMedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-self.small[0] + self.large[0]) / 2
```

### 80. Last Stone Weight
```python
def lastStoneWeight(stones):
    """
    Simulate smashing stones.
    Time: O(n log n), Space: O(n)
    """
    # Create max heap
    heap = [-stone for stone in stones]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        # Get two heaviest stones
        first = -heapq.heappop(heap)
        second = -heapq.heappop(heap)
        
        if first != second:
            heapq.heappush(heap, -(first - second))
    
    return -heap[0] if heap else 0
```

### 81. K Closest Points to Origin
```python
def kClosest(points, k):
    """
    Find k closest points to origin.
    Time: O(n log k), Space: O(k)
    """
    # Max heap (store negative distance)
    heap = []
    
    for x, y in points:
        dist = -(x*x + y*y)  # Negative for max heap
        
        if len(heap) < k:
            heapq.heappush(heap, (dist, x, y))
        else:
            heapq.heappushpop(heap, (dist, x, y))
    
    return [[x, y] for dist, x, y in heap]
```

### 82. Task Scheduler
```python
def leastInterval(tasks, n):
    """
    Calculate minimum intervals to schedule tasks.
    Time: O(n), Space: O(1)
    """
    from collections import Counter
    import heapq
    
    # Count frequencies
    freq = Counter(tasks)
    
    # Create max heap
    heap = [-count for count in freq.values()]
    heapq.heapify(heap)
    
    time = 0
    queue = deque()  # (count, ready_time)
    
    while heap or queue:
        time += 1
        
        # Execute task
        if heap:
            count = -heapq.heappop(heap)
            count -= 1
            if count > 0:
                queue.append((count, time + n))
        
        # Add ready tasks back to heap
        if queue and queue[0][1] == time:
            count, _ = queue.popleft()
            heapq.heappush(heap, -count)
    
    return time
```

---

## SECTION 9: GRAPH (Problems 83-92)

### 83. Number of Islands
```python
def numIslands(grid):
    """
    Count number of islands.
    Time: O(m*n), Space: O(m*n)
    """
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0
    
    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or
            grid[r][c] == '0' or (r, c) in visited):
            return
        
        visited.add((r, c))
        
        # Explore all 4 directions
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                islands += 1
                dfs(r, c)
    
    return islands
```

### 84. Clone Graph
```python
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node):
    """
    Clone an undirected graph.
    Time: O(n + e), Space: O(n)
    """
    if not node:
        return None
    
    # Map original nodes to cloned nodes
    mapping = {}
    
    def dfs(original):
        if original in mapping:
            return mapping[original]
        
        # Create clone
        clone = Node(original.val)
        mapping[original] = clone
        
        # Clone neighbors
        for neighbor in original.neighbors:
            clone.neighbors.append(dfs(neighbor))
        
        return clone
    
    return dfs(node)
```

### 85. Course Schedule
```python
def canFinish(numCourses, prerequisites):
    """
    Check if all courses can be completed.
    Time: O(n + e), Space: O(n + e)
    """
    from collections import defaultdict, deque
    
    # Build graph
    graph = defaultdict(list)
    in_degree = [0] * numCourses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    # BFS from courses with no prerequisites
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    completed = 0
    
    while queue:
        course = queue.popleft()
        completed += 1
        
        for next_course in graph[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)
    
    return completed == numCourses
```

### 86. Course Schedule II
```python
def findOrder(numCourses, prerequisites):
    """
    Find order to complete all courses.
    Time: O(n + e), Space: O(n + e)
    """
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    in_degree = [0] * numCourses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    result = []
    
    while queue:
        course = queue.popleft()
        result.append(course)
        
        for next_course in graph[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)
    
    return result if len(result) == numCourses else []
```

### 87. Pacific Atlantic Water Flow
```python
def pacificAtlantic(heights):
    """
    Find cells that can flow to both Pacific and Atlantic.
    Time: O(m*n), Space: O(m*n)
    """
    if not heights:
        return []
    
    rows, cols = len(heights), len(heights[0])
    pacific = set()
    atlantic = set()
    
    def dfs(r, c, visited, prev_height):
        if (r < 0 or r >= rows or c < 0 or c >= cols or
            (r, c) in visited or heights[r][c] < prev_height):
            return
        
        visited.add((r, c))
        
        # Explore all 4 directions
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        for dr, dc in directions:
            dfs(r + dr, c + dc, visited, heights[r][c])
    
    # Start from borders
    for r in range(rows):
        dfs(r, 0, pacific, heights[r][0])  # Left border
        dfs(r, cols-1, atlantic, heights[r][cols-1])  # Right border
    
    for c in range(cols):
        dfs(0, c, pacific, heights[0][c])  # Top border
        dfs(rows-1, c, atlantic, heights[rows-1][c])  # Bottom border
    
    return list(pacific.intersection(atlantic))
```

### 88. Graph Valid Tree
```python
def validTree(n, edges):
    """
    Check if graph is a valid tree.
    Time: O(n + e), Space: O(n + e)
    """
    if len(edges) != n - 1:
        return False
    
    # Build adjacency list
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # DFS to check connectivity and cycles
    visited = set()
    
    def dfs(node, parent):
        if node in visited:
            return False
        
        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            if not dfs(neighbor, node):
                return False
        
        return True
    
    # Check connectivity
    return dfs(0, -1) and len(visited) == n
```

### 89. Number of Connected Components
```python
def countComponents(n, edges):
    """
    Count connected components in undirected graph.
    Time: O(n + e), Space: O(n + e)
    """
    from collections import deque
    
    # Build adjacency list
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = set()
    components = 0
    
    for node in range(n):
        if node not in visited:
            components += 1
            
            # BFS to visit all nodes in component
            queue = deque([node])
            visited.add(node)
            
            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
    
    return components
```

### 90. Rotting Oranges
```python
def orangesRotting(grid):
    """
    Minimum minutes to rot all oranges.
    Time: O(m*n), Space: O(m*n)
    """
    from collections import deque
    
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_count = 0
    
    # Initialize queue with rotten oranges
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))  # (row, col, minutes)
            elif grid[r][c] == 1:
                fresh_count += 1
    
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    minutes = 0
    
    while queue:
        r, c, minutes = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and
                grid[nr][nc] == 1):
                grid[nr][nc] = 2
                fresh_count -= 1
                queue.append((nr, nc, minutes + 1))
    
    return minutes if fresh_count == 0 else -1
```

### 91. Word Ladder
```python
def ladderLength(beginWord, endWord, wordList):
    """
    Shortest transformation sequence from beginWord to endWord.
    Time: O(n * L²), Space: O(n * L)
    """
    from collections import deque
    from string import ascii_lowercase
    
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0
    
    queue = deque([(beginWord, 1)])  # (word, level)
    visited = set([beginWord])
    
    while queue:
        word, level = queue.popleft()
        
        # Try changing each character
        for i in range(len(word)):
            for char in ascii_lowercase:
                new_word = word[:i] + char + word[i+1:]
                
                if new_word == endWord:
                    return level + 1
                
                if new_word in wordSet and new_word not in visited:
                    visited.add(new_word)
                    queue.append((new_word, level + 1))
    
    return 0
```

### 92. Network Delay Time
```python
def networkDelayTime(times, n, k):
    """
    Time for signal to reach all nodes.
    Time: O(e log n), Space: O(n + e)
    """
    import heapq
    
    # Build graph
    graph = [[] for _ in range(n + 1)]
    for u, v, w in times:
        graph[u].append((v, w))
    
    # Dijkstra's algorithm
    distances = [float('inf')] * (n + 1)
    distances[k] = 0
    heap = [(0, k)]  # (distance, node)
    visited = set()
    
    while heap:
        dist, node = heapq.heappop(heap)
        
        if node in visited:
            continue
        
        visited.add(node)
        
        for neighbor, weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    
    max_time = max(distances[1:])
    return max_time if max_time != float('inf') else -1
```

---

## SECTION 10: DYNAMIC PROGRAMMING (Problems 93-100)

### 93. Climbing Stairs
```python
def climbStairs(n):
    """
    Number of ways to climb n stairs.
    Time: O(n), Space: O(1)
    """
    if n <= 2:
        return n
    
    first = 1
    second = 2
    
    for _ in range(3, n + 1):
        current = first + second
        first = second
        second = current
    
    return second
```

### 94. House Robber
```python
def rob(nums):
    """
    Maximum money without robbing adjacent houses.
    Time: O(n), Space: O(1)
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    # dp: max money up to current house
    prev2 = nums[0]
    prev1 = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        current = max(prev1, prev2 + nums[i])
        prev2 = prev1
        prev1 = current
    
    return prev1
```

### 95. House Robber II
```python
def robII(nums):
    """
    House robber with circular houses.
    Time: O(n), Space: O(1)
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    def rob_linear(start, end):
        if start > end:
            return 0
        if start == end:
            return nums[start]
        
        prev2 = nums[start]
        prev1 = max(nums[start], nums[start + 1])
        
        for i in range(start + 2, end + 1):
            current = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = current
        
        return prev1
    
    # Either rob first house or last house
    return max(rob_linear(0, len(nums) - 2),
               rob_linear(1, len(nums) - 1))
```

### 96. Coin Change
```python
def coinChange(coins, amount):
    """
    Minimum coins to make amount.
    Time: O(n * amount), Space: O(amount)
    """
    # dp[i] = min coins to make amount i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1
```

### 97. Longest Increasing Subsequence
```python
def lengthOfLIS(nums):
    """
    Length of longest increasing subsequence.
    Time: O(n log n), Space: O(n)
    """
    import bisect
    
    # tails[i] = minimum possible tail of increasing subsequence of length i+1
    tails = []
    
    for num in nums:
        # Find position to insert
        pos = bisect.bisect_left(tails, num)
        
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    
    return len(tails)
```

### 98. Longest Common Subsequence
```python
def longestCommonSubsequence(text1, text2):
    """
    Length of longest common subsequence.
    Time: O(m*n), Space: O(m*n)
    """
    m, n = len(text1), len(text2)
    
    # dp[i][j] = LCS of text1[:i] and text2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]
```

### 99. Partition Equal Subset Sum
```python
def canPartition(nums):
    """
    Can partition array into two equal sum subsets.
    Time: O(n * sum), Space: O(sum)
    """
    total_sum = sum(nums)
    
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    
    # dp[i] = can achieve sum i
    dp = [False] * (target + 1)
    dp[0] = True
    
    for num in nums:
        for i in range(target, num - 1, -1):
            if dp[i - num]:
                dp[i] = True
    
    return dp[target]
```

### 100. Edit Distance
```python
def minDistance(word1, word2):
    """
    Minimum operations to convert word1 to word2.
    Time: O(m*n), Space: O(m*n)
    """
    m, n = len(word1), len(word2)
    
    # dp[i][j] = min operations for word1[:i] to word2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base cases
    for i in range(m + 1):
        dp[i][0] = i  # Delete all characters
    for j in range(n + 1):
        dp[0][j] = j  # Insert all characters
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # Delete
                    dp[i][j-1],    # Insert
                    dp[i-1][j-1]   # Replace
                )
    
    return dp[m][n]
```

---

## 🎯 Summary for Python Backend Interview

### Most Important Concepts to Master:
1. **Time/Space Complexity Analysis** - Always mention Big O
2. **Recursion vs Iteration** - Know when to use which
3. **Data Structures** - Choose appropriate ones for each problem
4. **Edge Cases** - Empty inputs, single elements, large numbers
5. **In-place Operations** - Save space when possible
6. **Clean Code** - Readable, well-commented code

### Common Interview Question Patterns:
- **Two Pointers** (Arrays/strings)
- **Sliding Window** (Substring problems)
- **DFS/BFS** (Tree/Graph traversals)
- **Dynamic Programming** (Optimization problems)
- **Hash Maps** (Lookup/Counting problems)

### Tips for Success:
1. Practice explaining your solution as you code
2. Write clean, modular code with helper functions
3. Test with edge cases mentally
4. Consider trade-offs (time vs space)
5. Be ready to optimize your solution

**Good luck with your Python Backend interview! 🚀**

