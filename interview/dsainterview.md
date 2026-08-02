# Complete Advanced DSA Solutions (Problems 101-200)

I'll provide comprehensive solutions with detailed comments for all advanced problems.

---

## SECTION 1: SLIDING WINDOW (Problems 101-110)

### 101. Maximum Average Subarray I
```python
def findMaxAverage(nums, k):
    """
    Find maximum average of subarray of length k.
    Time: O(n), Space: O(1)
    """
    # Calculate sum of first window
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    # Slide window and update max
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum / k
```

### 102. Minimum Size Subarray Sum
```python
def minSubArrayLen(target, nums):
    """
    Find minimum length of subarray with sum >= target.
    Time: O(n), Space: O(1)
    """
    left = 0
    window_sum = 0
    min_length = float('inf')
    
    for right in range(len(nums)):
        window_sum += nums[right]
        
        # Shrink window while sum >= target
        while window_sum >= target:
            min_length = min(min_length, right - left + 1)
            window_sum -= nums[left]
            left += 1
    
    return min_length if min_length != float('inf') else 0
```

### 103. Longest Repeating Character Replacement
```python
def characterReplacement(s, k):
    """
    Longest substring with same characters after at most k replacements.
    Time: O(n), Space: O(1)
    """
    count = {}  # Character frequency in current window
    max_freq = 0  # Maximum frequency in current window
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # Add new character
        count[s[right]] = count.get(s[right], 0) + 1
        max_freq = max(max_freq, count[s[right]])
        
        # If window size - max_freq > k, shrink window
        while (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1
            # Update max_freq (optional but good for optimization)
            # max_freq = max(count.values())  # Uncomment for accuracy
        
        max_length = max(max_length, right - left + 1)
    
    return max_length
```

### 104. Permutation in String
```python
def checkInclusion(s1, s2):
    """
    Check if s1's permutation is substring of s2.
    Time: O(n), Space: O(1)
    """
    from collections import Counter
    
    if len(s1) > len(s2):
        return False
    
    # Count characters in s1
    s1_count = Counter(s1)
    window_count = Counter()
    
    # Initialize first window
    for i in range(len(s1)):
        window_count[s2[i]] += 1
    
    # Check first window
    if window_count == s1_count:
        return True
    
    # Slide window
    for i in range(len(s1), len(s2)):
        # Add new character
        window_count[s2[i]] += 1
        # Remove old character
        window_count[s2[i - len(s1)]] -= 1
        
        # Remove zero counts for clean comparison
        if window_count[s2[i - len(s1)]] == 0:
            del window_count[s2[i - len(s1)]]
        
        if window_count == s1_count:
            return True
    
    return False
```

### 105. Find All Anagrams in a String
```python
def findAnagrams(s, p):
    """
    Find all start indices of p's anagrams in s.
    Time: O(n), Space: O(1)
    """
    from collections import Counter
    
    if len(p) > len(s):
        return []
    
    p_count = Counter(p)
    window_count = Counter()
    result = []
    
    # Initialize first window
    for i in range(len(p)):
        window_count[s[i]] += 1
    
    if window_count == p_count:
        result.append(0)
    
    # Slide window
    for i in range(len(p), len(s)):
        window_count[s[i]] += 1
        window_count[s[i - len(p)]] -= 1
        
        if window_count[s[i - len(p)]] == 0:
            del window_count[s[i - len(p)]]
        
        if window_count == p_count:
            result.append(i - len(p) + 1)
    
    return result
```

### 106. Fruit Into Baskets
```python
def totalFruit(fruits):
    """
    Maximum number of fruits in two baskets.
    Time: O(n), Space: O(1)
    """
    from collections import defaultdict
    
    fruit_count = defaultdict(int)
    left = 0
    max_fruits = 0
    
    for right in range(len(fruits)):
        # Add fruit to window
        fruit_count[fruits[right]] += 1
        
        # If more than 2 types, shrink window
        while len(fruit_count) > 2:
            fruit_count[fruits[left]] -= 1
            if fruit_count[fruits[left]] == 0:
                del fruit_count[fruits[left]]
            left += 1
        
        max_fruits = max(max_fruits, right - left + 1)
    
    return max_fruits
```

### 107. Maximum Consecutive Ones III
```python
def longestOnes(nums, k):
    """
    Maximum consecutive ones after flipping at most k zeros.
    Time: O(n), Space: O(1)
    """
    left = 0
    zero_count = 0
    max_len = 0
    
    for right in range(len(nums)):
        # Count zeros in window
        if nums[right] == 0:
            zero_count += 1
        
        # If too many zeros, shrink window
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        
        max_len = max(max_len, right - left + 1)
    
    return max_len
```

### 108. Subarrays with K Different Integers
```python
def subarraysWithKDistinct(nums, k):
    """
    Count subarrays with exactly k different integers.
    Time: O(n), Space: O(n)
    """
    def at_most_k(nums, k):
        """Count subarrays with at most k distinct integers."""
        from collections import defaultdict
        count = defaultdict(int)
        left = 0
        result = 0
        
        for right in range(len(nums)):
            count[nums[right]] += 1
            
            while len(count) > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1
            
            result += right - left + 1
        
        return result
    
    # Exactly k = at most k - at most (k-1)
    return at_most_k(nums, k) - at_most_k(nums, k - 1)
```

### 109. Longest Ones After Replacement
```python
def longestOnesAfterReplacement(nums, k):
    """
    Longest subarray after replacing at most k zeros with ones.
    Time: O(n), Space: O(1)
    """
    # Same as problem 107
    return longestOnes(nums, k)
```

### 110. Sliding Window Median
```python
import bisect

def medianSlidingWindow(nums, k):
    """
    Median of each sliding window.
    Time: O(n * k), Space: O(k)
    """
    result = []
    window = sorted(nums[:k])
    
    # First window median
    if k % 2 == 1:
        result.append(window[k // 2])
    else:
        result.append((window[k // 2 - 1] + window[k // 2]) / 2)
    
    # Slide window
    for i in range(k, len(nums)):
        # Remove element leaving window
        window.remove(nums[i - k])
        # Insert new element
        bisect.insort(window, nums[i])
        
        # Calculate median
        if k % 2 == 1:
            result.append(window[k // 2])
        else:
            result.append((window[k // 2 - 1] + window[k // 2]) / 2)
    
    return result
```

---

## SECTION 2: TWO POINTERS (Problems 111-120)

### 111. Remove Element
```python
def removeElement(nums, val):
    """
    Remove all occurrences of val in-place.
    Time: O(n), Space: O(1)
    """
    write = 0  # Position to write non-val elements
    
    for read in range(len(nums)):
        if nums[read] != val:
            nums[write] = nums[read]
            write += 1
    
    return write
```

### 112. Squares of a Sorted Array
```python
def sortedSquares(nums):
    """
    Return sorted squares of array.
    Time: O(n), Space: O(n)
    """
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    pos = n - 1
    
    # Two pointer from ends
    while left <= right:
        left_square = nums[left] * nums[left]
        right_square = nums[right] * nums[right]
        
        if left_square > right_square:
            result[pos] = left_square
            left += 1
        else:
            result[pos] = right_square
            right -= 1
        pos -= 1
    
    return result
```

### 113. Backspace String Compare
```python
def backspaceCompare(s, t):
    """
    Compare strings after backspace processing.
    Time: O(n), Space: O(1)
    """
    def build_string(s):
        result = []
        for char in s:
            if char != '#':
                result.append(char)
            elif result:
                result.pop()
        return ''.join(result)
    
    return build_string(s) == build_string(t)
```

### 114. Sort Colors (Dutch National Flag)
```python
def sortColors(nums):
    """
    Sort array with 0,1,2 in-place.
    Time: O(n), Space: O(1)
    """
    # Three pointers
    low, mid, high = 0, 0, len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
```

### 115. Trapping Rain Water
```python
def trap(height):
    """
    Calculate trapped rain water.
    Time: O(n), Space: O(1)
    """
    if not height:
        return 0
    
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0
    
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    
    return water
```

### 116. Two Sum II (Sorted Array)
```python
def twoSum(numbers, target):
    """
    Find two numbers in sorted array.
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []
```

### 117. 4Sum
```python
def fourSum(nums, target):
    """
    Find all quadruplets that sum to target.
    Time: O(n³), Space: O(n)
    """
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 3):
        # Skip duplicates for i
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        for j in range(i + 1, n - 2):
            # Skip duplicates for j
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            
            # Two pointer for remaining two
            left, right = j + 1, n - 1
            
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                
                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    
                    # Skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    
    return result
```

### 118. Partition Labels
```python
def partitionLabels(s):
    """
    Partition string into maximum parts with same characters in same part.
    Time: O(n), Space: O(1)
    """
    # Last occurrence of each character
    last = {}
    for i, char in enumerate(s):
        last[char] = i
    
    result = []
    start = 0
    end = 0
    
    for i, char in enumerate(s):
        end = max(end, last[char])
        
        if i == end:
            result.append(end - start + 1)
            start = i + 1
    
    return result
```

### 119. Boats to Save People
```python
def numRescueBoats(people, limit):
    """
    Minimum boats to save people.
    Time: O(n log n), Space: O(1)
    """
    people.sort()
    left, right = 0, len(people) - 1
    boats = 0
    
    while left <= right:
        # Heavy person with lightest possible
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        boats += 1
    
    return boats
```

### 120. Interval List Intersections
```python
def intervalIntersection(firstList, secondList):
    """
    Find intersections of two interval lists.
    Time: O(n + m), Space: O(n + m)
    """
    i = j = 0
    result = []
    
    while i < len(firstList) and j < len(secondList):
        # Find intersection of current intervals
        start = max(firstList[i][0], secondList[j][0])
        end = min(firstList[i][1], secondList[j][1])
        
        if start <= end:
            result.append([start, end])
        
        # Move pointer with smaller end
        if firstList[i][1] < secondList[j][1]:
            i += 1
        else:
            j += 1
    
    return result
```

---

## SECTION 3: PREFIX SUM (Problems 121-130)

### 121. Running Sum of 1D Array
```python
def runningSum(nums):
    """
    Running sum of array.
    Time: O(n), Space: O(1)
    """
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums
```

### 122. Range Sum Query
```python
class NumArray:
    """
    Range sum query with prefix sums.
    Time: O(n) build, O(1) query
    """
    def __init__(self, nums):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)
    
    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]
```

### 123. Subarray Sum Equals K
```python
def subarraySum(nums, k):
    """
    Count subarrays with sum equal to k.
    Time: O(n), Space: O(n)
    """
    prefix_sum = 0
    count = 0
    sum_count = {0: 1}  # Sum -> frequency
    
    for num in nums:
        prefix_sum += num
        
        # Check if prefix_sum - k exists
        if prefix_sum - k in sum_count:
            count += sum_count[prefix_sum - k]
        
        # Add current prefix sum
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
    
    return count
```

### 124. Continuous Subarray Sum
```python
def checkSubarraySum(nums, k):
    """
    Check if there's subarray of length >= 2 with sum multiple of k.
    Time: O(n), Space: O(k)
    """
    remainder_map = {0: -1}  # Remainder -> index
    prefix_sum = 0
    
    for i, num in enumerate(nums):
        prefix_sum += num
        
        if k != 0:
            remainder = prefix_sum % k
        else:
            remainder = prefix_sum
        
        if remainder in remainder_map:
            if i - remainder_map[remainder] >= 2:
                return True
        else:
            remainder_map[remainder] = i
    
    return False
```

### 125. Pivot Index
```python
def pivotIndex(nums):
    """
    Find index where sum left = sum right.
    Time: O(n), Space: O(1)
    """
    total_sum = sum(nums)
    left_sum = 0
    
    for i, num in enumerate(nums):
        # Right sum = total_sum - left_sum - num
        if left_sum == total_sum - left_sum - num:
            return i
        left_sum += num
    
    return -1
```

### 126. Product of Array Except Self (Prefix Version)
```python
def productExceptSelf(nums):
    """
    Product of array except self (already solved as #4).
    Time: O(n), Space: O(1)
    """
    n = len(nums)
    result = [1] * n
    
    # Left products
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]
    
    # Right products
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
    
    return result
```

### 127. Corporate Flight Bookings
```python
def corpFlightBookings(bookings, n):
    """
    Difference array for flight bookings.
    Time: O(n + m), Space: O(n)
    """
    result = [0] * n
    
    for first, last, seats in bookings:
        result[first - 1] += seats
        if last < n:
            result[last] -= seats
    
    # Prefix sum
    for i in range(1, n):
        result[i] += result[i - 1]
    
    return result
```

### 128. Car Pooling
```python
def carPooling(trips, capacity):
    """
    Check if car has enough capacity.
    Time: O(n + max_distance), Space: O(max_distance)
    """
    max_distance = 0
    for trip in trips:
        max_distance = max(max_distance, trip[2])
    
    # Difference array
    passengers = [0] * (max_distance + 1)
    
    for num, start, end in trips:
        passengers[start] += num
        passengers[end] -= num
    
    # Prefix sum
    current = 0
    for i in range(max_distance + 1):
        current += passengers[i]
        if current > capacity:
            return False
    
    return True
```

### 129. Maximum Size Subarray Sum Equals K
```python
def maxSubArrayLen(nums, k):
    """
    Maximum length subarray with sum = k.
    Time: O(n), Space: O(n)
    """
    prefix_sum = 0
    sum_index = {0: -1}  # Sum -> earliest index
    max_len = 0
    
    for i, num in enumerate(nums):
        prefix_sum += num
        
        if prefix_sum - k in sum_index:
            max_len = max(max_len, i - sum_index[prefix_sum - k])
        
        if prefix_sum not in sum_index:
            sum_index[prefix_sum] = i
    
    return max_len
```

### 130. Count Number of Nice Subarrays
```python
def numberOfSubarrays(nums, k):
    """
    Count subarrays with exactly k odd numbers.
    Time: O(n), Space: O(n)
    """
    # Convert to 1 for odd, 0 for even
    # Then same as subarray sum equals k
    prefix_sum = 0
    count = 0
    sum_count = {0: 1}
    
    for num in nums:
        if num % 2 == 1:
            prefix_sum += 1
        
        if prefix_sum - k in sum_count:
            count += sum_count[prefix_sum - k]
        
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
    
    return count
```

---

## SECTION 4: MATRIX (Problems 131-140)

### 131. Set Matrix Zeroes
```python
def setZeroes(matrix):
    """
    Set entire row and column to zero if element is zero.
    Time: O(m*n), Space: O(1)
    """
    if not matrix:
        return
    
    rows, cols = len(matrix), len(matrix[0])
    first_row_zero = False
    first_col_zero = False
    
    # Check if first row/col have zeros
    for c in range(cols):
        if matrix[0][c] == 0:
            first_row_zero = True
            break
    
    for r in range(rows):
        if matrix[r][0] == 0:
            first_col_zero = True
            break
    
    # Use first row/col as markers
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0
    
    # Set zeros based on markers
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0
    
    # Set first row/col if needed
    if first_row_zero:
        for c in range(cols):
            matrix[0][c] = 0
    
    if first_col_zero:
        for r in range(rows):
            matrix[r][0] = 0
```

### 132. Spiral Matrix
```python
def spiralOrder(matrix):
    """
    Return matrix elements in spiral order.
    Time: O(m*n), Space: O(m*n)
    """
    if not matrix:
        return []
    
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # Traverse right
        for c in range(left, right + 1):
            result.append(matrix[top][c])
        top += 1
        
        # Traverse down
        for r in range(top, bottom + 1):
            result.append(matrix[r][right])
        right -= 1
        
        # Traverse left
        if top <= bottom:
            for c in range(right, left - 1, -1):
                result.append(matrix[bottom][c])
            bottom -= 1
        
        # Traverse up
        if left <= right:
            for r in range(bottom, top - 1, -1):
                result.append(matrix[r][left])
            left += 1
    
    return result
```

### 133. Rotate Image
```python
def rotate(matrix):
    """
    Rotate matrix 90 degrees clockwise in-place.
    Time: O(n²), Space: O(1)
    """
    n = len(matrix)
    
    # Transpose matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
```

### 134. Search a 2D Matrix
```python
def searchMatrix(matrix, target):
    """
    Search in sorted 2D matrix (row and column sorted).
    Time: O(log(m*n)), Space: O(1)
    """
    if not matrix or not matrix[0]:
        return False
    
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_val = matrix[mid // cols][mid % cols]
        
        if mid_val == target:
            return True
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False
```

### 135. Search a 2D Matrix II
```python
def searchMatrixII(matrix, target):
    """
    Search in 2D matrix where rows and columns are sorted.
    Time: O(m+n), Space: O(1)
    """
    if not matrix or not matrix[0]:
        return False
    
    rows, cols = len(matrix), len(matrix[0])
    r, c = 0, cols - 1  # Start from top-right
    
    while r < rows and c >= 0:
        if matrix[r][c] == target:
            return True
        elif matrix[r][c] > target:
            c -= 1
        else:
            r += 1
    
    return False
```

### 136. Game of Life
```python
def gameOfLife(board):
    """
    Conway's Game of Life in-place.
    Time: O(m*n), Space: O(1)
    """
    if not board or not board[0]:
        return
    
    rows, cols = len(board), len(board[0])
    directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]
    
    def count_live_neighbors(r, c):
        count = 0
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if board[nr][nc] == 1 or board[nr][nc] == -1:  # -1 means was alive
                    count += 1
        return count
    
    # First pass: mark cells that will change
    for r in range(rows):
        for c in range(cols):
            live_neighbors = count_live_neighbors(r, c)
            
            if board[r][c] == 1:  # Live cell
                if live_neighbors < 2 or live_neighbors > 3:
                    board[r][c] = -1  # Will die
            else:  # Dead cell
                if live_neighbors == 3:
                    board[r][c] = 2  # Will become alive
    
    # Second pass: apply changes
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == -1:
                board[r][c] = 0
            elif board[r][c] == 2:
                board[r][c] = 1
```

### 137. Flood Fill
```python
def floodFill(image, sr, sc, newColor):
    """
    Flood fill algorithm (DFS).
    Time: O(m*n), Space: O(m*n)
    """
    if not image:
        return image
    
    rows, cols = len(image), len(image[0])
    original_color = image[sr][sc]
    
    if original_color == newColor:
        return image
    
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if image[r][c] != original_color:
            return
        
        image[r][c] = newColor
        
        # Explore all 4 directions
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    
    dfs(sr, sc)
    return image
```

### 138. Word Search
```python
def exist(board, word):
    """
    Check if word exists in board (adjacent cells).
    Time: O(m*n*4^L), Space: O(L)
    """
    if not board or not board[0]:
        return False
    
    rows, cols = len(board), len(board[0])
    visited = set()
    
    def dfs(r, c, index):
        if index == len(word):
            return True
        
        if (r < 0 or r >= rows or c < 0 or c >= cols or
            (r, c) in visited or board[r][c] != word[index]):
            return False
        
        visited.add((r, c))
        
        # Explore all 4 directions
        found = (dfs(r + 1, c, index + 1) or
                 dfs(r - 1, c, index + 1) or
                 dfs(r, c + 1, index + 1) or
                 dfs(r, c - 1, index + 1))
        
        visited.remove((r, c))
        return found
    
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0] and dfs(r, c, 0):
                return True
    
    return False
```

### 139. Number of Islands (Already solved as #83)

### 140. Surrounded Regions
```python
def solve(board):
    """
    Capture surrounded regions by flipping 'O' to 'X'.
    Time: O(m*n), Space: O(m*n)
    """
    if not board or not board[0]:
        return
    
    rows, cols = len(board), len(board[0])
    
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
            return
        
        board[r][c] = '#'  # Mark as border-connected
        
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    
    # Mark all 'O' connected to border
    for r in range(rows):
        if board[r][0] == 'O':
            dfs(r, 0)
        if board[r][cols - 1] == 'O':
            dfs(r, cols - 1)
    
    for c in range(cols):
        if board[0][c] == 'O':
            dfs(0, c)
        if board[rows - 1][c] == 'O':
            dfs(rows - 1, c)
    
    # Flip remaining 'O' to 'X', restore '#' to 'O'
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O':
                board[r][c] = 'X'
            elif board[r][c] == '#':
                board[r][c] = 'O'
```

---

## SECTION 5: BACKTRACKING (Problems 141-150)

### 141. Subsets
```python
def subsets(nums):
    """
    Generate all subsets (power set).
    Time: O(2^n), Space: O(2^n)
    """
    result = []
    
    def backtrack(start, current):
        result.append(current[:])
        
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()
    
    backtrack(0, [])
    return result
```

### 142. Subsets II (with duplicates)
```python
def subsetsWithDup(nums):
    """
    Generate unique subsets with duplicates.
    Time: O(2^n), Space: O(2^n)
    """
    nums.sort()
    result = []
    
    def backtrack(start, current):
        result.append(current[:])
        
        for i in range(start, len(nums)):
            # Skip duplicates
            if i > start and nums[i] == nums[i - 1]:
                continue
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()
    
    backtrack(0, [])
    return result
```

### 143. Permutations
```python
def permute(nums):
    """
    Generate all permutations.
    Time: O(n*n!), Space: O(n!)
    """
    result = []
    
    def backtrack(current):
        if len(current) == len(nums):
            result.append(current[:])
            return
        
        for num in nums:
            if num not in current:
                current.append(num)
                backtrack(current)
                current.pop()
    
    backtrack([])
    return result
```

### 144. Permutations II (with duplicates)
```python
def permuteUnique(nums):
    """
    Generate unique permutations with duplicates.
    Time: O(n*n!), Space: O(n!)
    """
    nums.sort()
    result = []
    used = [False] * len(nums)
    
    def backtrack(current):
        if len(current) == len(nums):
            result.append(current[:])
            return
        
        for i in range(len(nums)):
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue
            
            used[i] = True
            current.append(nums[i])
            backtrack(current)
            current.pop()
            used[i] = False
    
    backtrack([])
    return result
```

### 145. Combination Sum
```python
def combinationSum(candidates, target):
    """
    Find combinations that sum to target (unlimited use).
    Time: O(2^n), Space: O(n)
    """
    result = []
    
    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        if remaining < 0:
            return
        
        for i in range(start, len(candidates)):
            current.append(candidates[i])
            backtrack(i, current, remaining - candidates[i])
            current.pop()
    
    backtrack(0, [], target)
    return result
```

### 146. Combination Sum II (unique combinations)
```python
def combinationSum2(candidates, target):
    """
    Find unique combinations (each used once).
    Time: O(2^n), Space: O(n)
    """
    candidates.sort()
    result = []
    
    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            
            current.append(candidates[i])
            backtrack(i + 1, current, remaining - candidates[i])
            current.pop()
    
    backtrack(0, [], target)
    return result
```

### 147. Letter Combinations of a Phone Number
```python
def letterCombinations(digits):
    """
    Generate letter combinations from phone digits.
    Time: O(3^n * 4^m), Space: O(n)
    """
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi',
        '5': 'jkl', '6': 'mno', '7': 'pqrs',
        '8': 'tuv', '9': 'wxyz'
    }
    
    result = []
    
    def backtrack(index, current):
        if index == len(digits):
            result.append(''.join(current))
            return
        
        for char in phone_map[digits[index]]:
            current.append(char)
            backtrack(index + 1, current)
            current.pop()
    
    backtrack(0, [])
    return result
```

### 148. Palindrome Partitioning
```python
def partition(s):
    """
    Partition string into palindromic substrings.
    Time: O(n*2^n), Space: O(n)
    """
    result = []
    
    def is_palindrome(left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
    def backtrack(start, current):
        if start == len(s):
            result.append(current[:])
            return
        
        for end in range(start, len(s)):
            if is_palindrome(start, end):
                current.append(s[start:end + 1])
                backtrack(end + 1, current)
                current.pop()
    
    backtrack(0, [])
    return result
```

### 149. Generate Parentheses
```python
def generateParenthesis(n):
    """
    Generate all valid parentheses combinations.
    Time: O(4^n / sqrt(n)), Space: O(n)
    """
    result = []
    
    def backtrack(open_count, close_count, current):
        if len(current) == 2 * n:
            result.append(current)
            return
        
        if open_count < n:
            backtrack(open_count + 1, close_count, current + '(')
        
        if close_count < open_count:
            backtrack(open_count, close_count + 1, current + ')')
    
    backtrack(0, 0, '')
    return result
```

### 150. N-Queens
```python
def solveNQueens(n):
    """
    Solve N-Queens problem.
    Time: O(n!), Space: O(n)
    """
    result = []
    board = [['.'] * n for _ in range(n)]
    cols = set()
    diag1 = set()  # r - c
    diag2 = set()  # r + c
    
    def backtrack(r):
        if r == n:
            result.append([''.join(row) for row in board])
            return
        
        for c in range(n):
            if c in cols or (r - c) in diag1 or (r + c) in diag2:
                continue
            
            # Place queen
            board[r][c] = 'Q'
            cols.add(c)
            diag1.add(r - c)
            diag2.add(r + c)
            
            backtrack(r + 1)
            
            # Remove queen
            board[r][c] = '.'
            cols.remove(c)
            diag1.remove(r - c)
            diag2.remove(r + c)
    
    backtrack(0)
    return result
```

---

## SECTION 6: BINARY SEARCH ADVANCED (Problems 151-160)

### 151. Search Insert Position
```python
def searchInsert(nums, target):
    """
    Find insert position for target.
    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left
```

### 152. Guess Number Higher or Lower
```python
def guessNumber(n):
    """
    Guess number with API.
    Time: O(log n), Space: O(1)
    """
    # Assume guess API exists
    def guess(num):
        # This is a placeholder
        pass
    
    left, right = 1, n
    
    while left <= right:
        mid = (left + right) // 2
        result = guess(mid)
        
        if result == 0:
            return mid
        elif result == -1:
            right = mid - 1
        else:
            left = mid + 1
    
    return -1
```

### 153. First Bad Version
```python
def firstBadVersion(n):
    """
    Find first bad version.
    Time: O(log n), Space: O(1)
    """
    def isBadVersion(version):
        # This is a placeholder
        pass
    
    left, right = 1, n
    
    while left < right:
        mid = (left + right) // 2
        
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    
    return left
```

### 154. Koko Eating Bananas
```python
def minEatingSpeed(piles, h):
    """
    Find minimum eating speed.
    Time: O(n log max), Space: O(1)
    """
    def can_eat_all(speed):
        hours = 0
        for pile in piles:
            hours += (pile + speed - 1) // speed
        return hours <= h
    
    left, right = 1, max(piles)
    
    while left < right:
        mid = (left + right) // 2
        
        if can_eat_all(mid):
            right = mid
        else:
            left = mid + 1
    
    return left
```

### 155. Capacity to Ship Packages
```python
def shipWithinDays(weights, days):
    """
    Find minimum ship capacity.
    Time: O(n log sum), Space: O(1)
    """
    def can_ship(capacity):
        current_weight = 0
        days_needed = 1
        
        for weight in weights:
            if current_weight + weight > capacity:
                days_needed += 1
                current_weight = 0
            current_weight += weight
        
        return days_needed <= days
    
    left, right = max(weights), sum(weights)
    
    while left < right:
        mid = (left + right) // 2
        
        if can_ship(mid):
            right = mid
        else:
            left = mid + 1
    
    return left
```

### 156. Split Array Largest Sum
```python
def splitArray(nums, k):
    """
    Minimize largest subarray sum when splitting into k parts.
    Time: O(n log sum), Space: O(1)
    """
    def can_split(max_sum):
        current_sum = 0
        parts = 1
        
        for num in nums:
            if current_sum + num > max_sum:
                parts += 1
                current_sum = 0
            current_sum += num
        
        return parts <= k
    
    left, right = max(nums), sum(nums)
    
    while left < right:
        mid = (left + right) // 2
        
        if can_split(mid):
            right = mid
        else:
            left = mid + 1
    
    return left
```

### 157. Find Peak Element
```python
def findPeakElement(nums):
    """
    Find peak element in mountain array.
    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    
    return left
```

### 158. Median of Two Sorted Arrays
```python
def findMedianSortedArrays(nums1, nums2):
    """
    Find median of two sorted arrays.
    Time: O(log(min(m,n))), Space: O(1)
    """
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    total = m + n
    half = total // 2
    
    left, right = 0, m
    
    while left <= right:
        i = (left + right) // 2  # Partition in nums1
        j = half - i  # Partition in nums2
        
        nums1_left = nums1[i - 1] if i > 0 else float('-inf')
        nums1_right = nums1[i] if i < m else float('inf')
        nums2_left = nums2[j - 1] if j > 0 else float('-inf')
        nums2_right = nums2[j] if j < n else float('inf')
        
        if nums1_left <= nums2_right and nums2_left <= nums1_right:
            if total % 2 == 1:
                return min(nums1_right, nums2_right)
            else:
                return (max(nums1_left, nums2_left) + 
                       min(nums1_right, nums2_right)) / 2
        elif nums1_left > nums2_right:
            right = i - 1
        else:
            left = i + 1
    
    return 0
```

### 159. Find First and Last Position
```python
def searchRange(nums, target):
    """
    Find first and last position of target.
    Time: O(log n), Space: O(1)
    """
    def find_first():
        left, right = 0, len(nums) - 1
        first = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                first = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return first
    
    def find_last():
        left, right = 0, len(nums) - 1
        last = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                last = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return last
    
    return [find_first(), find_last()]
```

### 160. Search a 2D Matrix (Already solved as #134)

---

## SECTION 7: GREEDY (Problems 161-170)

### 161. Jump Game
```python
def canJump(nums):
    """
    Check if can reach last index.
    Time: O(n), Space: O(1)
    """
    max_reach = 0
    
    for i, jump in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + jump)
    
    return True
```

### 162. Jump Game II
```python
def jump(nums):
    """
    Minimum jumps to reach last index.
    Time: O(n), Space: O(1)
    """
    jumps = 0
    current_end = 0
    farthest = 0
    
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        
        if i == current_end:
            jumps += 1
            current_end = farthest
    
    return jumps
```

### 163. Gas Station
```python
def canCompleteCircuit(gas, cost):
    """
    Find starting gas station.
    Time: O(n), Space: O(1)
    """
    total_gas = sum(gas)
    total_cost = sum(cost)
    
    if total_gas < total_cost:
        return -1
    
    current_gas = 0
    start = 0
    
    for i in range(len(gas)):
        current_gas += gas[i] - cost[i]
        
        if current_gas < 0:
            start = i + 1
            current_gas = 0
    
    return start
```

### 164. Candy
```python
def candy(ratings):
    """
    Minimum candies to distribute.
    Time: O(n), Space: O(n)
    """
    n = len(ratings)
    candies = [1] * n
    
    # Left to right
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1
    
    # Right to left
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
    
    return sum(candies)
```

### 165. Assign Cookies
```python
def findContentChildren(g, s):
    """
    Maximum satisfied children.
    Time: O(n log n), Space: O(1)
    """
    g.sort()
    s.sort()
    
    child = 0
    cookie = 0
    
    while child < len(g) and cookie < len(s):
        if s[cookie] >= g[child]:
            child += 1
        cookie += 1
    
    return child
```

### 166. Lemonade Change
```python
def lemonadeChange(bills):
    """
    Can give change with 5, 10, 20 bills.
    Time: O(n), Space: O(1)
    """
    five = ten = 0
    
    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            if five == 0:
                return False
            five -= 1
            ten += 1
        else:  # bill == 20
            if ten > 0 and five > 0:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    
    return True
```

### 167. Queue Reconstruction by Height
```python
def reconstructQueue(people):
    """
    Reconstruct queue based on height and count.
    Time: O(n²), Space: O(n)
    """
    people.sort(key=lambda x: (-x[0], x[1]))
    result = []
    
    for person in people:
        result.insert(person[1], person)
    
    return result
```

### 168. Non-overlapping Intervals
```python
def eraseOverlapIntervals(intervals):
    """
    Minimum intervals to remove to make non-overlapping.
    Time: O(n log n), Space: O(1)
    """
    if not intervals:
        return 0
    
    intervals.sort(key=lambda x: x[1])
    count = 0
    end = intervals[0][1]
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < end:
            count += 1
        else:
            end = intervals[i][1]
    
    return count
```

### 169. Minimum Number of Arrows to Burst Balloons
```python
def findMinArrowShots(points):
    """
    Minimum arrows to burst all balloons.
    Time: O(n log n), Space: O(1)
    """
    if not points:
        return 0
    
    points.sort(key=lambda x: x[1])
    arrows = 1
    end = points[0][1]
    
    for start, balloon_end in points[1:]:
        if start > end:
            arrows += 1
            end = balloon_end
    
    return arrows
```

### 170. Hand of Straights
```python
def isNStraightHand(hand, groupSize):
    """
    Can be arranged in groups of consecutive cards.
    Time: O(n log n), Space: O(n)
    """
    if len(hand) % groupSize != 0:
        return False
    
    from collections import Counter
    count = Counter(hand)
    
    for card in sorted(hand):
        if count[card] > 0:
            for i in range(card, card + groupSize):
                if count[i] == 0:
                    return False
                count[i] -= 1
    
    return True
```

---

## SECTION 8: INTERVALS (Problems 171-180)

### 171. Merge Intervals
```python
def merge(intervals):
    """
    Merge overlapping intervals.
    Time: O(n log n), Space: O(n)
    """
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]
    
    for start, end in intervals[1:]:
        if start <= result[-1][1]:
            result[-1][1] = max(result[-1][1], end)
        else:
            result.append([start, end])
    
    return result
```

### 172. Insert Interval
```python
def insert(intervals, newInterval):
    """
    Insert interval into sorted non-overlapping intervals.
    Time: O(n), Space: O(n)
    """
    result = []
    i = 0
    start, end = newInterval
    
    # Add intervals before newInterval
    while i < len(intervals) and intervals[i][1] < start:
        result.append(intervals[i])
        i += 1
    
    # Merge overlapping intervals
    while i < len(intervals) and intervals[i][0] <= end:
        start = min(start, intervals[i][0])
        end = max(end, intervals[i][1])
        i += 1
    
    result.append([start, end])
    
    # Add remaining intervals
    while i < len(intervals):
        result.append(intervals[i])
        i += 1
    
    return result
```

### 173. Meeting Rooms
```python
def canAttendMeetings(intervals):
    """
    Check if one person can attend all meetings.
    Time: O(n log n), Space: O(1)
    """
    intervals.sort(key=lambda x: x[0])
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    
    return True
```

### 174. Meeting Rooms II
```python
def minMeetingRooms(intervals):
    """
    Minimum rooms needed for meetings.
    Time: O(n log n), Space: O(n)
    """
    if not intervals:
        return 0
    
    starts = sorted([i[0] for i in intervals])
    ends = sorted([i[1] for i in intervals])
    
    rooms = 0
    end_ptr = 0
    
    for start in starts:
        if start < ends[end_ptr]:
            rooms += 1
        else:
            end_ptr += 1
    
    return rooms
```

### 175. Employee Free Time
```python
def employeeFreeTime(schedule):
    """
    Find free time common to all employees.
    Time: O(n log n), Space: O(n)
    """
    # Flatten schedule
    intervals = []
    for employee in schedule:
        intervals.extend(employee)
    
    intervals.sort(key=lambda x: x[0])
    
    # Merge intervals
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    
    # Find gaps
    result = []
    for i in range(1, len(merged)):
        if merged[i][0] > merged[i - 1][1]:
            result.append([merged[i - 1][1], merged[i][0]])
    
    return result
```

### 176. Remove Covered Intervals
```python
def removeCoveredIntervals(intervals):
    """
    Remove intervals covered by others.
    Time: O(n log n), Space: O(n)
    """
    intervals.sort(key=lambda x: (x[0], -x[1]))
    count = 0
    end = 0
    
    for start, interval_end in intervals:
        if interval_end > end:
            count += 1
            end = interval_end
    
    return count
```

### 177. Minimum Interval
```python
def minInterval(intervals, queries):
    """
    Find minimum interval containing each query.
    Time: O(n log n + q log q), Space: O(n + q)
    """
    import heapq
    
    intervals.sort()
    queries = sorted([(q, i) for i, q in enumerate(queries)])
    
    result = [-1] * len(queries)
    heap = []
    j = 0
    
    for q, idx in queries:
        # Add intervals starting before or at q
        while j < len(intervals) and intervals[j][0] <= q:
            start, end = intervals[j]
            heapq.heappush(heap, (end - start + 1, end))
            j += 1
        
        # Remove intervals ending before q
        while heap and heap[0][1] < q:
            heapq.heappop(heap)
        
        if heap:
            result[idx] = heap[0][0]
    
    return result
```

### 178. Interval Scheduling (Maximum Non-overlapping)
```python
def intervalScheduling(intervals):
    """
    Maximum number of non-overlapping intervals.
    Time: O(n log n), Space: O(1)
    """
    intervals.sort(key=lambda x: x[1])
    count = 0
    end = float('-inf')
    
    for start, interval_end in intervals:
        if start >= end:
            count += 1
            end = interval_end
    
    return count
```

### 179. Erase Overlapping Intervals (Already solved as #168)

### 180. Summary Ranges
```python
def summaryRanges(nums):
    """
    Return summary ranges.
    Time: O(n), Space: O(n)
    """
    if not nums:
        return []
    
    result = []
    start = nums[0]
    
    for i in range(1, len(nums) + 1):
        if i == len(nums) or nums[i] != nums[i - 1] + 1:
            if start == nums[i - 1]:
                result.append(str(start))
            else:
                result.append(f"{start}->{nums[i - 1]}")
            
            if i < len(nums):
                start = nums[i]
    
    return result
```

---

## SECTION 9: TRIE (Problems 181-185)

### 181. Implement Trie
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    """
    Implement Trie (Prefix Tree).
    Time: O(L) for operations, Space: O(total characters)
    """
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word
    
    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
```

### 182. Design Add and Search Words
```python
class WordDictionary:
    """
    Word dictionary with wildcard '.' support.
    Time: O(26^L) for search, Space: O(total characters)
    """
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
    
    def search(self, word):
        def dfs(node, index):
            if index == len(word):
                return node.is_word
            
            char = word[index]
            if char == '.':
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(node.children[char], index + 1)
        
        return dfs(self.root, 0)
```

### 183. Word Search II
```python
def findWords(board, words):
    """
    Find all words in board.
    Time: O(m*n*4^L), Space: O(total characters)
    """
    # Build Trie
    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
        node.word = word
    
    rows, cols = len(board), len(board[0])
    result = []
    visited = set()
    
    def dfs(r, c, node):
        if (r < 0 or r >= rows or c < 0 or c >= cols or
            (r, c) in visited or board[r][c] not in node.children):
            return
        
        visited.add((r, c))
        node = node.children[board[r][c]]
        
        if node.is_word:
            result.append(node.word)
            node.is_word = False  # Avoid duplicates
        
        # Explore all 4 directions
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        for dr, dc in directions:
            dfs(r + dr, c + dc, node)
        
        visited.remove((r, c))
    
    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root)
    
    return result
```

### 184. Replace Words
```python
def replaceWords(dictionary, sentence):
    """
    Replace words with their roots.
    Time: O(n), Space: O(n)
    """
    # Build Trie
    root = TrieNode()
    for word in dictionary:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
    
    # Process sentence
    result = []
    for word in sentence.split():
        node = root
        root_found = False
        
        for i, char in enumerate(word):
            if char not in node.children:
                break
            node = node.children[char]
            if node.is_word:
                result.append(word[:i + 1])
                root_found = True
                break
        
        if not root_found:
            result.append(word)
    
    return ' '.join(result)
```

### 185. Longest Word in Dictionary
```python
def longestWord(words):
    """
    Find longest word that can be built one character at a time.
    Time: O(n log n), Space: O(n)
    """
    words.sort()
    word_set = set()
    result = ""
    
    for word in words:
        if len(word) == 1 or word[:-1] in word_set:
            if len(word) > len(result):
                result = word
            word_set.add(word)
    
    return result
```

---

## SECTION 10: UNION FIND / DISJOINT SET (Problems 186-190)

### 186. Number of Provinces
```python
def findCircleNum(isConnected):
    """
    Count provinces (connected components).
    Time: O(n²), Space: O(n)
    """
    n = len(isConnected)
    parent = list(range(n))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[py] = px
            return True
        return False
    
    provinces = n
    for i in range(n):
        for j in range(i + 1, n):
            if isConnected[i][j] and union(i, j):
                provinces -= 1
    
    return provinces
```

### 187. Redundant Connection
```python
def findRedundantConnection(edges):
    """
    Find edge that creates cycle.
    Time: O(n α(n)), Space: O(n)
    """
    n = len(edges)
    parent = list(range(n + 1))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        parent[py] = px
        return True
    
    for u, v in edges:
        if not union(u, v):
            return [u, v]
    
    return []
```

### 188. Accounts Merge
```python
def accountsMerge(accounts):
    """
    Merge accounts with same email.
    Time: O(n log n), Space: O(n)
    """
    from collections import defaultdict
    
    parent = list(range(len(accounts)))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[py] = px
    
    # Map email to account index
    email_to_account = {}
    
    for i, account in enumerate(accounts):
        for email in account[1:]:
            if email in email_to_account:
                union(i, email_to_account[email])
            else:
                email_to_account[email] = i
    
    # Group emails by root parent
    merged = defaultdict(set)
    for i, account in enumerate(accounts):
        root = find(i)
        for email in account[1:]:
            merged[root].add(email)
    
    # Build result
    result = []
    for root, emails in merged.items():
        result.append([accounts[root][0]] + sorted(emails))
    
    return result
```

### 189. Evaluate Division
```python
def calcEquation(equations, values, queries):
    """
    Evaluate division equations.
    Time: O(n + q), Space: O(n)
    """
    from collections import defaultdict
    
    graph = defaultdict(dict)
    
    # Build graph
    for (a, b), value in zip(equations, values):
        graph[a][b] = value
        graph[b][a] = 1 / value
    
    def dfs(start, end, visited):
        if start not in graph or end not in graph:
            return -1.0
        if start == end:
            return 1.0
        
        visited.add(start)
        
        for neighbor, value in graph[start].items():
            if neighbor not in visited:
                result = dfs(neighbor, end, visited)
                if result != -1.0:
                    return value * result
        
        return -1.0
    
    results = []
    for a, b in queries:
        results.append(dfs(a, b, set()))
    
    return results
```

### 190. Satisfiability of Equality Equations
```python
def equationsPossible(equations):
    """
    Check if equations are satisfiable.
    Time: O(n), Space: O(1)
    """
    parent = list(range(26))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[py] = px
    
    # Process equality equations
    for eq in equations:
        if eq[1] == '=':
            x = ord(eq[0]) - ord('a')
            y = ord(eq[3]) - ord('a')
            union(x, y)
    
    # Check inequality equations
    for eq in equations:
        if eq[1] == '!':
            x = ord(eq[0]) - ord('a')
            y = ord(eq[3]) - ord('a')
            if find(x) == find(y):
                return False
    
    return True
```

---

## SECTION 11: BIT MANIPULATION (Problems 191-200)

### 191. Single Number
```python
def singleNumber(nums):
    """
    Find number appearing once (others appear twice).
    Time: O(n), Space: O(1)
    """
    result = 0
    for num in nums:
        result ^= num
    return result
```

### 192. Number of 1 Bits
```python
def hammingWeight(n):
    """
    Count number of 1 bits.
    Time: O(number of bits), Space: O(1)
    """
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
```

### 193. Counting Bits
```python
def countBits(n):
    """
    Count bits for numbers from 0 to n.
    Time: O(n), Space: O(n)
    """
    result = [0] * (n + 1)
    
    for i in range(1, n + 1):
        # dp[i] = dp[i >> 1] + (i & 1)
        result[i] = result[i >> 1] + (i & 1)
    
    return result
```

### 194. Reverse Bits
```python
def reverseBits(n):
    """
    Reverse 32-bit integer bits.
    Time: O(1), Space: O(1)
    """
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result
```

### 195. Missing Number (Bit Version)
```python
def missingNumber(nums):
    """
    Find missing number using XOR.
    Time: O(n), Space: O(1)
    """
    n = len(nums)
    result = n
    
    for i, num in enumerate(nums):
        result ^= i ^ num
    
    return result
```

### 196. Sum of Two Integers
```python
def getSum(a, b):
    """
    Add two numbers without using + operator.
    Time: O(1), Space: O(1)
    """
    while b != 0:
        # XOR gives sum without carry
        # AND gives carry
        carry = (a & b) << 1
        a = a ^ b
        b = carry
    
    return a
```

### 197. Bitwise AND of Numbers Range
```python
def rangeBitwiseAnd(left, right):
    """
    Bitwise AND of numbers in range.
    Time: O(1), Space: O(1)
    """
    shift = 0
    
    # Find common prefix
    while left < right:
        left >>= 1
        right >>= 1
        shift += 1
    
    return left << shift
```

### 198. Power of Two
```python
def isPowerOfTwo(n):
    """
    Check if n is power of two.
    Time: O(1), Space: O(1)
    """
    if n <= 0:
        return False
    return n & (n - 1) == 0
```

### 199. Power of Four
```python
def isPowerOfFour(n):
    """
    Check if n is power of four.
    Time: O(1), Space: O(1)
    """
    if n <= 0:
        return False
    
    # Check power of two and position of set bit
    return (n & (n - 1) == 0) and (n & 0x55555555) != 0
```

### 200. Divide Two Integers
```python
def divide(dividend, divisor):
    """
    Divide two integers without multiplication/division.
    Time: O(log n), Space: O(1)
    """
    # Handle overflow
    if dividend == -2**31 and divisor == -1:
        return 2**31 - 1
    
    # Get sign
    negative = (dividend < 0) ^ (divisor < 0)
    
    # Work with positive numbers
    dividend = abs(dividend)
    divisor = abs(divisor)
    
    quotient = 0
    
    while dividend >= divisor:
        temp = divisor
        multiple = 1
        
        # Double divisor until it exceeds dividend
        while dividend >= (temp << 1):
            temp <<= 1
            multiple <<= 1
        
        dividend -= temp
        quotient += multiple
    
    return -quotient if negative else quotient
```

---

## 🎯 Top 30 Must-Solve Problems for Python Backend Interview

```python
# These 30 problems are critical for Django/FastAPI interviews
must_solve = {
    "Arrays": [1, 4, 5],  # Two Sum, Product Except Self, Max Subarray
    "Strings": [16, 17, 20],  # Valid Anagram, Group Anagrams, Longest Substring
    "Hash": [35, 37],  # Top K Frequent, Longest Consecutive
    "Stack": [39, 40, 41],  # Valid Parentheses, Min Stack, Daily Temperatures
    "Linked List": [51, 52, 53],  # Reverse, Merge, Cycle
    "Trees": [61, 66, 68],  # Max Depth, Level Order, Validate BST
    "Graph": [83, 84, 85],  # Number of Islands, Clone Graph, Course Schedule
    "DP": [93, 94, 96],  # Climbing Stairs, House Robber, Coin Change
    "Intervals": [171, 172],  # Merge Intervals, Insert Interval
    "LRU": [201]  # Not in list but essential
}
```

### Key Takeaways for Python Backend Interview:

1. **Focus on Problem Patterns** - Most problems are variations of core patterns
2. **Time Complexity Matters** - Always mention Big O for your solutions
3. **Space Optimization** - In-place operations when possible
4. **Edge Cases** - Empty input, single element, negative numbers
5. **Clean Code** - Use clear variable names and helper functions

### Study Strategy:
1. **Week 1-2**: Arrays, Strings, Hash Tables
2. **Week 3-4**: Linked Lists, Trees, Graphs
3. **Week 5-6**: DP, Backtracking, Intervals
4. **Week 7-8**: Advanced topics and review
5. **Practice daily**: 2-3 problems with explanation

**Good luck with your preparation! You've got this! 🚀**

