"""
=========================================================
LeetCode 3731 - Find Missing Elements
=========================================================

Problem
-------

You are given an array of UNIQUE integers.

Originally, the array contained every integer
in a continuous range.

However, some numbers were removed.

The smallest and largest numbers of the
original range are still present.

Return all missing numbers in sorted order.

---------------------------------------------------------

Example 1

Input

nums = [1,4,2,5]

Original range

1 2 3 4 5

Present

1 2 4 5

Missing

3

Output

[3]

---------------------------------------------------------

Example 2

Input

nums = [7,8,6,9]

Original range

6 7 8 9

Nothing is missing.

Output

[]

---------------------------------------------------------

Example 3

Input

nums = [5,1]

Original range

1 2 3 4 5

Present

1 5

Missing

2 3 4

Output

[2,3,4]

=========================================================
Observation
=========================================================

The smallest and largest numbers are guaranteed
to exist.

So,

minimum = min(nums)

maximum = max(nums)

Every number between them SHOULD exist.

We only need to find which ones are missing.

=========================================================
Idea
=========================================================

Step 1

Find

minimum value

maximum value

----------------------------------

Step 2

Store every number in a set.

Why?

Searching in a set takes

O(1)

time.

----------------------------------

Step 3

Loop from

minimum + 1

to

maximum - 1

If a number is NOT in the set,

it is missing.

Add it to the answer.

=========================================================
Algorithm
=========================================================

Find minimum

Find maximum

Convert nums into a set

For every number from minimum+1 to maximum-1

    If number not in set

        Add to answer

Return answer

=========================================================
Dry Run
=========================================================

nums = [1,4,2,5]

Step 1

minimum = 1

maximum = 5

----------------------------------

Step 2

Set

{1,2,4,5}

----------------------------------

Loop

2

Exists

Skip

------------------

3

Not present

Answer

[3]

------------------

4

Exists

Skip

Finished

Output

[3]

=========================================================
Another Dry Run
=========================================================

nums = [5,1]

minimum = 1

maximum = 5

Set

{1,5}

Loop

2

Missing

Answer

[2]

------------------

3

Missing

Answer

[2,3]

------------------

4

Missing

Answer

[2,3,4]

Finished

=========================================================
Time Complexity
=========================================================

Finding min and max

O(n)

Creating set

O(n)

Loop

O(max-min)

Since constraints are small,

Overall

O(n)

=========================================================
Space Complexity
=========================================================

Set

O(n)

=========================================================
Python Solution
=========================================================
"""

from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:

        mn = min(nums)
        mx = max(nums)

        s = set(nums)

        ans = []

        for num in range(mn + 1, mx):

            if num not in s:
                ans.append(num)

        return ans


# -------------------------------------------------------
# Example Usage
# -------------------------------------------------------

if __name__ == "__main__":

    s = Solution()

    print(s.findMissingElements([1,4,2,5]))   # [3]
    print(s.findMissingElements([7,8,6,9]))   # []
    print(s.findMissingElements([5,1]))       # [2,3,4]
    print(s.findMissingElements([1,2,3,4,5])) # []
    print(s.findMissingElements([10, 12, 11, 15])) # [13, 14]
    print(s.findMissingElements([100, 105, 102, 101])) # [103, 104] 
    